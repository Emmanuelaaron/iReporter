from flask import Blueprint
from api.controllers.users_controller import UsersController

my_user = UsersController()
users_blueprint = Blueprint("Users", __name__, url_prefix="/api/v1")

@users_blueprint.route('/')
def index():
    return "you're welcome to ireporter"

@users_blueprint.route("/signup", methods=["POST"])
def signup_user():
    return my_user.signupUser()
