from flask import Blueprint, render_template, request, redirect, url_for, jsonify

authentication_bp = Blueprint('authentication_bp', __name__, template_folder='templates', static_folder='static')

@authentication_bp.route("/login", methods=["GET"])
def login():
    return render_template("authentication/login.html")

@authentication_bp.route("/login_user", methods=["POST"])
def loginUser():
    if request.method == "POST":
        data = request.get_json()
        if data:
            email = data.get("email")
            password = data.get("password")

        if email == "admin@test.com" and password == "123":
            return redirect(url_for("assitant_bp.assistant"))
        else:
            return render_template("authentication/login.html")
        
@authentication_bp.route("/signup", methods=["GET"])
def signup():
    return render_template("authentication/signup.html")

@authentication_bp.route("/signup_user", methods=["POST"])
def signupUser():

    data = request.get_json()

    if not data:
        return jsonify({"message": "Invalid request"}), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    repassword = data.get("repassword")

    print(name, email, password, repassword)

    if password != repassword:
        return jsonify({"message": "Passwords do not match"}), 400

    # Normally you would save user in DB here

    return jsonify({
        "message": "Account created successfully",
        "redirect": url_for("dashboard_bp.dashboard")
    }), 200

@authentication_bp.route("/forgot-password", methods=["GET"])
def forgot_password():
    return render_template("authentication/forgot_password.html")

@authentication_bp.route("/forgot_password_user", methods=["POST"])
def forgotPasswordUser():
    if request.method == "POST":
        data = request.get_json()
        if data:
            email = data.get("email")
            print(email)

    return jsonify({
        "message": "email send to your email id",
        "redirect": url_for("authentication_bp.login")
    }), 200