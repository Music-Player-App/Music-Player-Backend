print("auth_routes.py loaded")

from flask import Blueprint
from controllers.auth_controller import (
    register_user,
    login_user,
    get_profile,
    update_profile,
    delete_profile,
    change_password  
)

auth_bp = Blueprint("auth", __name__, url_prefix="/api")

auth_bp.route("/register", methods=["POST"])(register_user)
auth_bp.route("/login", methods=["POST"])(login_user)
auth_bp.route("/profile", methods=["GET"])(get_profile)
auth_bp.route("/profile", methods=["PUT"])(update_profile)
auth_bp.route("/profile", methods=["DELETE"])(delete_profile)
auth_bp.route("/profile/password", methods=["PUT"])(change_password) 
