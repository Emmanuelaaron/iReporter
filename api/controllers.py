from .models import users, Users, incidents, Incidents
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

        user_details = [firstname, lastname, email, password, username]
        for detail in user_details:
            if Validating_string.is_space(detail) or not Validating_string.characters(detail):
                 return jsonify({
                    "message": "All fields must be filled!"
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

        incidents_details = [incidenceType, location, comment, user_id]
        for incident in incidents_details:
            if type(incident) is str:
                if Validating_string.is_space(incident) or not Validating_string.characters(incident):
                    return jsonify({
                        "message": "All fields must be filled!"
                        }), 400
        if len(Users.get_all_users()) == 0:
            return jsonify({
                "message": "user not found!"
            }), 400
        for incident in incidents:
            if incident["incidenceType"] == incidenceType and incident["location"] == location:
                return jsonify({
                    "message": "Incidence already captured!"
                }), 400

        for user in Users.get_all_users():
            if user["user_id"] != user_id:
                return jsonify({
                    "message": "invalid user id"
                }), 400
        my_incident = Incidents(incidenceType, location, comment)
        message = my_incident.create_incidence(user_id)
        return jsonify(message), 201

    @staticmethod
    def get_all_red_flags():
        if len(Incidents.get_all_incidents()) == 0:
            return jsonify({
                "message": "No incidents so far!"
            }), 201
        return jsonify(Incidents.get_all_incidents()), 201

    @staticmethod
    def get_specific_red_flag(flag_id):
        if len(Incidents.get_all_incidents()) == 0:
            return jsonify({
                "message": "No incidents!"
            })
        for incident in Incidents.get_all_incidents():
            if incident["flag_id"] != flag_id:
                return jsonify({
                    "message": "Flag id does not exist!"
                }), 400
        return jsonify(incident), 201

    @staticmethod
    def delete_specific_red_flag(flag_id):
        if len(Incidents.get_all_incidents()) == 0:
            return jsonify({
                "message": "No incidents!"
            }), 400
        for incident in Incidents.get_all_incidents():
            if incident["flag_id"] != flag_id:
                return jsonify({
                    "message": "Flag id does not exist!"
                }), 400
            Incidents.get_all_incidents().remove(incident)
            return jsonify({
                "message": "Sucessfully deleted!"
            })