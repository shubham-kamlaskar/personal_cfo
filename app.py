from flask import Flask
import logging
from dotenv import load_dotenv
load_dotenv()

from src.routes.landing_page_route import landing_page_bp
from src.routes.authentication_route import authentication_bp
from src.routes.dashboard_route import dashboard_bp
from src.routes.tax_filling_route import tax_filling_bp
from src.routes.investments_route import investments_bp
from src.routes.documents_route import documents_bp
from src.routes.calculator_route import calculator_bp
from src.routes.assistant_route import assistant_bp

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

app.register_blueprint(landing_page_bp)
app.register_blueprint(authentication_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(tax_filling_bp)
app.register_blueprint(investments_bp)
app.register_blueprint(documents_bp)
app.register_blueprint(calculator_bp)
app.register_blueprint(assistant_bp)


if __name__ == "__main__":
    app.run(debug=True)