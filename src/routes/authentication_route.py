from flask import Blueprint, render_template, request, redirect

authentication_bp = Blueprint('authentication_bp', __name__, template_folder='templates', static_folder='static')

@authentication_bp.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == "admin@test.com" and password == "123":
            return redirect("/assistant")

    return render_template("login.html")

@authentication_bp.route("/signup", methods=["GET","POST"])
def signup():

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        print(name,email,password)

    return render_template("signup.html")


@authentication_bp.route("/forgot-password", methods=["GET","POST"])
def forgot_password():

    if request.method == "POST":
        email = request.form.get("email")
        print(email)

    return render_template("forgot_password.html")