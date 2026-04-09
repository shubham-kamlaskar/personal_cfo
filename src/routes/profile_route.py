from flask import Blueprint, render_template
from src.database_provider.fetch_user_info import user

user_profile_bp = Blueprint('user_profile_bp', __name__, template_folder='templates', static_folder='static')

@user_profile_bp.route('/profile', methods=["GET"])
def profile():
    user_data = user
    return render_template("user_profile/profile.html", user=user_data)