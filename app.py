from flask import Flask, request, jsonify, render_template
import os
import logging
from dotenv import load_dotenv
load_dotenv()
from src.agent_provider.langchain_agent import get_agent_client
from src.tool_provider.tool_calls import tools
from src.llm_provider.ollama_llm import llm_client
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

# Initialize once (better performance)
llm = llm_client(llm_model_name=os.getenv('LLM_MODEL_NAME'), llm_temperature=float(os.getenv('LLM_TEMPERATURE')))
agent = get_agent_client(llm, tools)


@app.route("/", methods=["GET"])
def dashboard():
    logging.info('Health check endpoint hit')
    return render_template("dashboard.html")

@app.route("/tax_filling", methods=["GET"])
def tax_filling():
    return render_template("tax_filling.html")

@app.route("/investments", methods=["GET"])
def investments():
    return render_template("investments.html")

@app.route("/documents", methods=["GET"])
def documents():
    return render_template("documents.html")

@app.route("/calculator", methods=["GET"])
def calculator():
    return render_template("calculator.html")

@app.route("/assistant", methods=["GET"])
def assistant():
    return render_template("assistant.html")


@app.route("/query", methods=["POST"])
def query():
    try:
        logging.info('Query endpoint hit')
        data = request.get_json(silent=True)

        if not data or "query" not in data:
            return jsonify({"error": "query field required"}), 400

        user_query = data["query"]
        logging.info(f"Query received: {user_query}")
        response = agent.invoke(
            {"messages": [{"role": "user", "content": user_query}]}
        )
        logging.info("Agent response received")
        answer = response["messages"][-1].content
        logging.info(f"Answer generated: {answer}")
        return jsonify({
            "query": user_query,
            "response": answer
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)