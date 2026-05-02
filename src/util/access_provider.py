from functools import wraps
from flask import session, url_for, redirect, abort

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("authentication_bp.login"))
        return f(*args, **kwargs)
    return decorated_function


def login_required_with_rbac(allowed_roles=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):

            # Check login
            if "user" not in session:
                return redirect(url_for("authentication_bp.login"))

            # Check RBAC role
            if allowed_roles:
                user_role = session.get("user").get("rbac_role")

                if user_role not in allowed_roles:
                    return abort(403)   # Forbidden

            return f(*args, **kwargs)

        return decorated_function
    return decorator