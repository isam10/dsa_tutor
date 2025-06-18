from flask import render_template, Blueprint, session, redirect, url_for
from dsa_tutor.curriculum import DSACurriculum
from dsa_tutor.database import DatabaseManager

learning_bp = Blueprint("learning", __name__)
db_manager = DatabaseManager()
curriculum = DSACurriculum() # <--- ENSURE THIS LINE IS PRESENT

@learning_bp.route("/modules")
def modules():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("main.index"))

    user_progress = db_manager.get_user_progress(user_id)
    modules_data = curriculum.get_all_modules() # <--- USE curriculum INSTANCE
    return render_template("modules.html", modules=modules_data, user_progress=user_progress)

@learning_bp.route("/module/<int:module_id>")
def module(module_id):
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("main.index"))

    module_info = curriculum.get_module_info(module_id) # <--- USE curriculum INSTANCE
    if not module_info:
        return render_template("error.html", message="Module not found.")

    user_progress = db_manager.get_user_progress(user_id) # <--- ENSURE THIS LINE IS PRESENT
    return render_template("module.html", module=module_info, user_progress=user_progress)

@learning_bp.route("/module/<int:module_id>/topic/<topic_title>")
def topic(module_id, topic_title):
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("main.index"))
    user_progress = db_manager.get_user_progress(user_id) # <--- ENSURE THIS LINE IS PRESENT
    module_info = curriculum.get_module_info(module_id) # <--- USE curriculum INSTANCE
    if not module_info or topic_title not in module_info["topics"]:
        return render_template("error.html", message="Topic not found.")

    topic_content = curriculum.get_topic_content(module_id, topic_title) # <--- USE curriculum INSTANCE
    
    # Update user progress: mark topic as completed
    completed_topics = user_progress["completed_topics"]
    if topic_title not in completed_topics:
        completed_topics.append(topic_title)
        db_manager.update_user_progress(user_id, completed_topics=completed_topics)

    return render_template("topic.html", module=module_info, topic_title=topic_title, topic_content=topic_content)
