from flask import render_template, Blueprint, session
from dsa_tutor.curriculum import DSACurriculum
from dsa_tutor.database import DatabaseManager
import uuid
main_bp = Blueprint("main", __name__)
db_manager = DatabaseManager()

@main_bp.route("/")
def index():
    user_id = session.get("user_id")
    if not user_id:
        user_id = str(uuid.uuid4())
        session["user_id"] = user_id

    user_progress = db_manager.get_user_progress(user_id)
    modules = DSACurriculum.get_all_modules()
    return render_template("index.html", modules=modules, user_progress=user_progress)

@main_bp.route("/about")
def about():
    return render_template("about.html")

@main_bp.route("/contact")
def contact():
    return render_template("contact.html")


