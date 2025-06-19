from flask import render_template, Blueprint, request, jsonify, session
from dsa_tutor.gemini_api import GeminiAPI
import os

agent_bp = Blueprint("agent", __name__)
gemini_api = GeminiAPI(api_key=os.getenv("GEMINI_API_KEY"))

@agent_bp.route("/dsa_agent")
def dsa_agent():
    return render_template("agent.html")

@agent_bp.route("/ask_agent", methods=["POST"])
def ask_agent():
    user_query = request.json.get("query")
    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    prompt = f"You are a DSA tutor agent. Provide a detailed explanation and solution for the following DSA problem or concept: {user_query}. Include Python code examples where applicable."
    response = gemini_api.generate_response(prompt)
    return jsonify({"response": response})


