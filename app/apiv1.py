from flask import Blueprint
from flask_restplus import Api

from app.controller.assignment_controller import api as assignment_ns

blueprint = Blueprint("api_v1", __name__, url_prefix="/api/v1")
api = Api(
    blueprint,
    title="assignment",
    version="1.0",
    description="Author: tanpk",
)
api.add_namespace(assignment_ns, path="/assignment")
