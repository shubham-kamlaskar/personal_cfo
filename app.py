from flask import Flask
import warnings
warnings.filterwarnings('ignore')
import sentry_sdk
from flask_cors import CORS

from src.routes.product.landing_page_route import landing_page_bp
from src.routes.authentication_route import authentication_bp
from src.routes.dashboard_route import dashboard_bp
from src.routes.tax_filling_route import tax_filling_bp
from src.routes.investments_route import investments_bp
from src.routes.documents_route import documents_bp
from src.routes.calculator_route import calculator_bp
from src.routes.assistant_route import assistant_bp
from src.routes.profile_route import user_profile_bp
from src.routes.client.client_dashboard_route import client_dashboard_bp
from src.routes.admin.dashboard_route import admin_dashboard_bp

sentry_sdk.init(
    dsn="https://a06064aaa11af0dea8206f744b21b006@o4511268270440448.ingest.us.sentry.io/4511268272603136",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    # Enable sending logs to Sentry
    enable_logs=True,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profile_session_sample_rate to 1.0 to profile 100%
    # of profile sessions.
    profile_session_sample_rate=1.0,
    # Set profile_lifecycle to "trace" to automatically
    # run the profiler on when there is an active transaction
    profile_lifecycle="trace",
)

app = Flask(__name__)
cors = CORS(app)
app.secret_key = "your_secret_key"


app.register_blueprint(landing_page_bp)
app.register_blueprint(authentication_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(tax_filling_bp)
app.register_blueprint(investments_bp)
app.register_blueprint(documents_bp)
app.register_blueprint(calculator_bp)
app.register_blueprint(assistant_bp)
app.register_blueprint(user_profile_bp)
app.register_blueprint(client_dashboard_bp)
app.register_blueprint(admin_dashboard_bp)



if __name__ == "__main__":
    app.run(debug=True)
