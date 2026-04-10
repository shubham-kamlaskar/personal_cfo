from flask import Blueprint, render_template, request, jsonify
from src.util.calculation_helper import TaxEngine

tax_engine = TaxEngine()

calculator_bp = Blueprint('calculator_bp', __name__, template_folder='templates', static_folder='static')

@calculator_bp.route("/<user_id>/calculator", methods=["GET"])
def calculator(user_id):
    return render_template("calculator.html", user_id=user_id)

@calculator_bp.route("/tax_calculator", methods=["POST"])
def tax_calculator():
    if request.method == "POST":
        data = request.get_json()
        if data:
            age = data.get('age')
            gross_income = float(data.get('gross', 0))
            std = float(data.get('std', 0))
            d80c = float(data.get('d80c', 0))
            if d80c > 150000:
                d80c = 150000
            d80d = float(data.get('d80d', 0))
            if d80d > 150000:
                d80d = 150000
            hra = float(data.get('hra', 0))
            hl = float(data.get('hl', 0))
            if hl > 200000:
                hl = 200000
            nps = float(data.get('nps', 0))
            regime = str(data.get('regime'))

            deductions = d80c + d80d + hra + hl + nps
            old_total_deductions = std + deductions

            old_base_tax, old_extra_cess, old_tax = tax_engine.old_regime_tax_calculation(
                total_income=gross_income,
                deductions=old_total_deductions
            )
            new_base_tax, new_extra_cess, new_tax = tax_engine.new_regime_tax_calculation(
                total_income=gross_income
            )

            if regime == "old_regime":
                selected_regime = "Old"
                selected_tax = old_tax
                selected_extra_cess = old_extra_cess
                selected_base_tax = old_base_tax
                total_deductions = old_total_deductions
                taxable_income = max(0.0, gross_income - old_total_deductions)
            else:
                selected_regime = "New"
                selected_tax = new_tax
                selected_extra_cess = new_extra_cess
                selected_base_tax = new_base_tax
                total_deductions = std
                taxable_income = max(0.0, gross_income - std)

            return jsonify({
                "selected_regime": selected_regime,
                "gross": round(gross_income, 2),
                "taxable_income": round(taxable_income, 2),
                "total_tax": round(selected_tax, 2),
                "total_deductions": round(total_deductions, 2),
                "tax_before_cess": round(selected_base_tax, 2),
                "cess": round(selected_extra_cess, 2),
                "old_regime_tax": round(old_tax, 2),
                "new_regime_tax": round(new_tax, 2)
            })

    return jsonify({"error": "Invalid request"}), 400
