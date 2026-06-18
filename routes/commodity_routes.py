from flask import Blueprint, jsonify, request

from services.commodity_service import (
    get_commodities_by_type
)

commodity_bp = Blueprint(
    "commodity",
    __name__
)

@commodity_bp.route(
    "/api/commodities",
    methods=["GET"]
)
def get_commodities():

    type_param = request.args.get("type")

    if not type_param:
        return jsonify({
            "error": "type query parameter is required"
        }), 400

    result = get_commodities_by_type(type_param)

    if not result:
        return jsonify({
            "message": "No data found"
        }), 404

    return jsonify(result)