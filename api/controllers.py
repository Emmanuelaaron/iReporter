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
            })
        if Validating_string.is_space(lastname) or not Validating_string.characters(lastname):
            return jsonify({
                "message": "lastname is required!"
            })
        if Validating_string.is_space(email) or not Validating_string.characters(email):
            return jsonify({
                "message": "email is required!"
            })
        if Validating_string.is_space(password) or not Validating_string.characters(password):
            return jsonify({
                "message": "password is required!"
            })
        if Validating_string.is_space(username) or not Validating_string.characters(username):
            return jsonify({
                "message": "username is required!"
            })

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
        return jsonify (my_account.signup())