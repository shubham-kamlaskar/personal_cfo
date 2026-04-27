import os
from dotenv import load_dotenv
import logging

from flask import Blueprint, render_template, request, jsonify
from src.ai_agent.langchain_agent import AgentProvider
from src.database.infodb.service.mongo_client import MongoDBClient
from src.database.infodb.service.conversation_history_service import HistoryClient
from src.util.access_provider import login_required
from src.ai_agent.langchain_agent import AgentProvider

load_dotenv()

agent_provider = AgentProvider()
mongodb_client = MongoDBClient()
history_client = HistoryClient()
db_name = str(os.getenv('DB_NAME'))
conversation_collection = str(os.getenv("CONVERSATION_COLLETION"))
logger = logging.getLogger(__name__)

assistant_bp = Blueprint('assistant_bp', __name__, template_folder='templates', static_folder='static')

@assistant_bp.route("/<user_id>/assistant", methods=["GET"])
@login_required
def assistant(user_id: str):
    try:
        conv_history = history_client.get_user_conversation_history(user_id)
        
        return render_template(
            "employee/assistant.html",
            user_id=user_id,
            conv_history=conv_history
        )
    except Exception as e:
        logger.error(f"An error occured in assistant route: {str(e)}")


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
            "response": answer,
            
        })

    except Exception as e:
        logger.error(f"An error occured in Query functions, {str(e)}")
        return jsonify({
            "error": str(e)
        }), 500