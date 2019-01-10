from flask import Blueprint
from api.controllers.incidents_controller import IncidentsController
from api.controllers.users_controller import UsersController

my_user = UsersController()
my_incident = IncidentsController()
incidents_blueprint = Blueprint("Incidents", __name__, url_prefix="/api/v1")

@incidents_blueprint.route("/red-flags", methods=["POST"])
def create_red():
    return IncidentsController.create_red_flag()

@incidents_blueprint.route("/red-flags")
def get_all_flags():
    return IncidentsController.get_all_red_flags()

@incidents_blueprint.route("/red-flags/<int:flag_id>")
def get_specific_red_flag(flag_id):
    return my_incident.get_specific_red_flag(flag_id)

@incidents_blueprint.route("/red-flags/<int:flag_id>", methods=["DELETE"])
def delete_specific_red_flag(flag_id):
    return IncidentsController.delete_specific_red_flag(flag_id)

@incidents_blueprint.route("/red-flags/<int:flag_id>/comment", methods=["PATCH"])
def edit_comment_specific_flag(flag_id):
    return IncidentsController.edit_comment_specific_red_flag(flag_id)

@incidents_blueprint.route("/red-flags/<int:flag_id>/location", methods=["PATCH"])
def edit_location_specific_flag(flag_id):
    return IncidentsController.edit_location_specific_red_flag(flag_id)