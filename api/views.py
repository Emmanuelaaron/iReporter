from flask import Flask
from api.controllers import UsersController


app = Flask(__name__)

@app.route("/")
def index():
    return "you're welcome to ireporter"

@app.route("/signup", methods=["POST"])
def signup_user():
    return UsersController.signupUser()
    


