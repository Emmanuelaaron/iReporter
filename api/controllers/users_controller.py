from api.models.users_model import User, Users
from flask import jsonify, request
from api.validation import Validating_string, email_validator

users_list = Users()
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

        if not email_validator.validate_email(email):
            return jsonify({
                "message": "Invalid email"
            })
        user_details = [firstname, lastname, email, password, username]
        for detail in user_details:
            if Validating_string.is_space(detail) or not Validating_string.characters(detail):
                 return jsonify({
                     "status": 400,
                    "message": "All fields must be filled!"
                    }), 400
        
        for user in users_list.get_all_users():
            if user["username"] == username or\
            user["email"] == email:
                return jsonify({
                    "status": 200,
                    "message": "username or already exists! Choose another one"
                }), 200
        my_account = User(firstname, lastname, othernames, email, password, username)
        my_account = my_account.signup()
        my_account["users_id"] = len(users_list.get_all_users()) + 1
        users_list.add_user(my_account)

        return jsonify({
            "status": 201,
            "message": "You've signed up sucessfully!",
            "data": my_account
        }), 201


