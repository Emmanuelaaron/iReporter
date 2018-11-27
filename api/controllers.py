from api.models import users, Users, incidents, Incidents
from flask import jsonify, request
from api.validation import Validating_string

class UsersController:

    @staticmethod
    def signupUser():
        data = request.get_json()
        firstname = data.get("firstname")
        lastname = data.get("lastname")
        othernames = data.get("othernames")
        email = data.get("email")
        password = data.get("password")
        username = data.get("username")
        
        if Validating_string.is_space(firstname) or not Validating_string.characters(firstname):
            return jsonify({
                "message": "firstname is required!"
            }), 400
        if Validating_string.is_space(lastname) or not Validating_string.characters(lastname):
            return jsonify({
                "message": "lastname is required!"
            }), 400
        if Validating_string.is_space(email) or not Validating_string.characters(email):
            return jsonify({
                "message": "email is required!"
            }), 400
        if Validating_string.is_space(password) or not Validating_string.characters(password):
            return jsonify({
                "message": "password is required!"
            }), 400
        if Validating_string.is_space(username) or not Validating_string.characters(username):
            return jsonify({
                "message": "username is required!"
            }), 400

        for user in Users.get_all_users():
            if user["username"] == username:
                return jsonify({
                    "message": "username already exists! Choose another one"
                })
            if user["email"] == email:
                return jsonify({
                    "message": "email already exists!"
                })
        my_account = Users(firstname, lastname, othernames, email, password, username)
        return jsonify (my_account.signup()), 201

class IncidentsController:

    @staticmethod
    def create_red_flag():
        data = request.get_json()
        incidenceType = data.get("incidenceType")
        location = data.get("location")
        comment = data.get("comment")
        user_id = data.get("user_id")

        for user in Users.get_all_users():
            if user["user_id"] != user_id:
                return jsonify({
                    "message": "invalid user id"
                }), 400
        my_incident = Incidents(incidenceType, location, comment)
        message = my_incident.create_incidence(user_id)
        return jsonify(message)