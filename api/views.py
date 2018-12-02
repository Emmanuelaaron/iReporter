from flask import Flask
from .controllers import UsersController, IncidentsController

my_user = UsersController()
my_incident = IncidentsController()
app = Flask(__name__)

@app.route("/")
def index():
    return "you're welcome to ireporter"

@app.route("/api/v1/signup", methods=["POST"])
def signup_user():
    return my_user.signupUser()

@app.route("/api/v1/red-flags", methods=["POST"])
def create_red():
    return IncidentsController.create_red_flag()

@app.route("/api/v1/red-flags")
def get_all_flags():
    return IncidentsController.get_all_red_flags()

@app.route("/api/v1/red-flags/<int:flag_id>")
def get_specific_red_flag(flag_id):
    return my_incident.get_specific_red_flag(flag_id)

@app.route("/api/v1/red-flags/<int:flag_id>", methods=["DELETE"])
def delete_specific_red_flag(flag_id):
    return IncidentsController.delete_specific_red_flag(flag_id)