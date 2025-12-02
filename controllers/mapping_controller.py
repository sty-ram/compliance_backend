from flask import Blueprint, request, jsonify, session
from models.mappings import MAPPINGS
from services.db_service import get_dummy_data_from_db
mapping = Blueprint("mapping", __name__)
print("MAPPING BLUEPRINT LOADED")

@mapping.route("/get_mappings", methods=["POST"])
def get_map():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    country = data.get("country")
    entity = data.get("entity")
    product = data.get("product")

    try:
        result = MAPPINGS[country][entity][product]
        return jsonify(result)
    except:
        return jsonify({"error": "Invalid combination"}), 400
@mapping.route("/get_countries", methods=["GET"]) # written to get list of countries
def get_countries():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    countries = list(MAPPINGS.keys())
    return jsonify(countries)

#route to get entities for a given country


@mapping.route("/get_dummy_data", methods=["GET"])
def get_dummy():
    data = get_dummy_data_from_db()
    return jsonify(data), 200
