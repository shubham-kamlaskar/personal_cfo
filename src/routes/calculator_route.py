from flask import Blueprint, render_template, request, jsonify

calculator_bp = Blueprint('calculator_bp', __name__, template_folder='templates', static_folder='static')

@calculator_bp.route("/calculator", methods=["GET"])
def calculator():
    return render_template("calculator.html")

@calculator_bp.route("/tax_calculator", methods=["POST"])
def tax_calculator():
    if request.method == "POST":
        data = request.get_json(silent=True)
        if data:
            age = int(data.get('age'))
            regime = str(data.get('regime'))
            gross_income = float(data.get('gross'))
            standard_deduction = int(data.get('std'))
            d80c = float(data.get('d80c'))
            d80d = float(data.get('d80d'))
            hra = float(data.get('hra'))
            hl = float(data.get('hl'))
            nps = float(data.get('nps'))
    return jsonify({'response':144484})