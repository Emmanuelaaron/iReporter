from flask import Flask
from api.controllers import UsersController


app = Flask(__name__)

@app.route("/")
def index():
    return "you're welcome to ireporter"

@app.route("/api/v1/signup", methods=["POST"])
def signup_user():
    return UsersController.signupUser()
    


