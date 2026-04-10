import os
from dotenv import load_dotenv
import logging

from flask import Blueprint, render_template, request, jsonify
from src.agent_provider.langchain_agent import AgentProvider
from src.util.log_adapter import setup_logger

load_dotenv()

agent_provider = AgentProvider()
logger = logging.getLogger(__name__)

assistant_bp = Blueprint('assistant_bp', __name__, template_folder='templates', static_folder='static')

@assistant_bp.route("/<user_id>/assistant", methods=["GET"])
def assistant(user_id: str):
    return render_template("assistant.html", user_id=user_id)


@assistant_bp.route("/<user_id>/query", methods=["POST"])
async def query(user_id: str):
    try:
        data = request.get_json(silent=True)

        if not data or "query" not in data:
            return jsonify({"error": "query field required"}), 400

        user_query = data.get("query")
        
        answer = await agent_provider.get_agent_response(user_query=user_query, user_id=user_id)
        logger.info("Answer is generated.")
        return jsonify({
            "query": user_query,
            "response": answer
        })

    except Exception as e:
        print(f"An error occured in Query functions, {str(e)}")
        return jsonify({
            "error": str(e)
        }), 500