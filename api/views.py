from flask import Flask
from api.controllers import UsersController, IncidentsController


app = Flask(__name__)

@app.route("/")
def index():
    return "you're welcome to ireporter"

@app.route("/api/v1/signup", methods=["POST"])
def signup_user():
    return UsersController.signupUser()

@app.route("/api/v1/red-flag", methods=["POST"])
def create_red():
    return IncidentsController.create_red_flag()
    


