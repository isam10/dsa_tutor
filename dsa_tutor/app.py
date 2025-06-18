import os
from flask import Flask
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    # Get the absolute path to the directory containing app.py
    base_dir = os.path.abspath(os.path.dirname(__file__))
    # Construct the path to the templates folder
    template_folder = os.path.join(base_dir, 'templates')

    app = Flask(__name__, template_folder=template_folder)
    app.config.from_object("dsa_tutor.config.Config")

    # Register blueprints
    from dsa_tutor.routes.main_routes import main_bp
    from dsa_tutor.routes.learning_routes import learning_bp
    from dsa_tutor.routes.agent_routes import agent_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(learning_bp)
    app.register_blueprint(agent_bp)

    return app
