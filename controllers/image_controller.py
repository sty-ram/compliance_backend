#  created for image upload and retrieval

from flask import Blueprint, request, jsonify, session
from services.db_service import upload_image_to_db, fetch_user_images

images = Blueprint("images", __name__)

@images.route("/upload_image", methods=["POST"])
def upload_image():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file"}), 400

    username = session["user"]
    result = upload_image_to_db(username, file)
    return jsonify(result), 200


@images.route("/get_images", methods=["GET"])
def get_images():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    username = session["user"]
    imgs = fetch_user_images(username)
    return jsonify(imgs), 200
