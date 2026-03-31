import os
from dotenv import load_dotenv
load_dotenv()

import html

from flask import Blueprint, render_template, request, jsonify
from src.agent_provider.langchain_agent import get_agent_client
from src.tool_provider.tool_calls import tools
from src.llm_provider.ollama_llm import llm_client

# Initialize once (better performance)
llm = llm_client(llm_model_name=os.getenv('LLM_MODEL_NAME'), llm_temperature=float(os.getenv('LLM_TEMPERATURE')))
agent = get_agent_client(llm, tools)

assistant_bp = Blueprint('assistant_bp', __name__, template_folder='templates', static_folder='static')

@assistant_bp.route("/assistant", methods=["GET"])
def assistant():
    return render_template("assistant.html")


@assistant_bp.route("/query", methods=["POST"])
def query():
    try:
        data = request.get_json(silent=True)

        if not data or "query" not in data:
            return jsonify({"error": "query field required"}), 400

        user_query = data.get("query")
        response = agent.invoke(
                {
                    "messages": [{"role": "user", "content": user_query}],
                    "user_id": "user_123",
                    "preferences": {"theme": "dark"}
                },
                {"configurable": {"thread_id": "1"}})
    
        answer = html.escape(response["messages"][-1].content)

        return jsonify({
            "query": user_query,
            "response": answer
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500