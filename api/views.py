from flask import Flask
from api.controllers import UsersController, IncidentsController


app = Flask(__name__)

@app.route("/")
def index():
    return "you're welcome to ireporter"

@app.route("/api/v1/signup", methods=["POST"])
def signup_user():
    return UsersController.signupUser()

@app.route("/api/v1/red-flags", methods=["POST"])
def create_red():
    return IncidentsController.create_red_flag()

@app.route("/api/v1/red-flags")
def get_all_flags():
    return IncidentsController.get_all_red_flags()

@app.route("/api/v1/red-flags/<int:flag_id>")
def get_specific_red_flag(flag_id):
    return IncidentsController.get_specific_red_flag(flag_id)

@app.route("/api/v1/red-flags/<int:flag_id>", methods=["DELETE"])
def delete_specific_red_flag(flag_id):
    return IncidentsController.delete_specific_red_flag(flag_id)