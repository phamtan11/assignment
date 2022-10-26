from flask import jsonify, request
from flask_restplus import Resource, Namespace, fields

from app.service.assignment_service import Assignment

assignment = Assignment()

api = Namespace("assignment", description="assignment operations")

add_pool_object = api.model(
    "add_pool", {
        "poolId": fields.Integer(
            required=True, description="poolId"), "poolValues": fields.List(
                fields.Integer, required=True, description="poolValues")})

query_object = api.model(
    "query",
    {
        "poolId": fields.Integer(required=True, description="poolId"),
        "percentile": fields.Float(required=True, description="percentile")
    }
)


@api.route("/add")
class AddPool(Resource):
    @api.expect(add_pool_object, validate=True)
    def post(self):
        data = request.json
        status = assignment.add_pool(data)
        return jsonify({"status": status})


@api.route("/query")
class Query(Resource):
    @api.expect(query_object, validate=True)
    def post(self):
        data = request.json
        quantile, count_element = assignment.query(data)
        return jsonify({"quantile": quantile,
                        "count_elements": count_element})
