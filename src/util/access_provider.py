from functools import wraps
from flask import session, url_for, redirect

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("authentication_bp.login"))
        return f(*args, **kwargs)
    return decorated_function