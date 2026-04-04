from flask import Blueprint, render_template, request, jsonify
from src.util.calculation_helper import TaxEngine

tax_engine = TaxEngine()

calculator_bp = Blueprint('calculator_bp', __name__, template_folder='templates', static_folder='static')

@calculator_bp.route("/calculator", methods=["GET"])
def calculator():
    return render_template("calculator.html")

@calculator_bp.route("/tax_calculator", methods=["POST"])
def tax_calculator():
    if request.method == "POST":
        data = request.get_json()
        if data:
            age = data.get('age')
            gross_income = float(data.get('gross'))
            d80c = float(data.get('d80c'))
            d80d = float(data.get('d80d'))
            hra = float(data.get('hra'))
            hl = float(data.get('hl'))
            nps = float(data.get('nps'))
            
            regime = str(data.get('regime'))
            
            deducations = d80c + d80d + hra + hl + nps
            
            old_base_tax, old_extra_cess, old_tax = tax_engine.old_regime_tax_calculation(total_income=gross_income, deductions=deducations)
            new_base_tax, new_extra_cess, new_tax = tax_engine.new_regime_tax_calculation(total_income=gross_income)
            
            if regime == "old_regime":
                regime="old"
                standard_deduction=50000
                selected_tax = old_tax
                selected_extra_cess = old_extra_cess
                selected_base_tax = old_base_tax
                comparison_tax = new_tax
            else:
                regime="new"
                standard_deduction=75000
                selected_tax = new_tax
                selected_extra_cess = new_extra_cess
                selected_base_tax = new_base_tax
                comparison_tax = old_tax
            
    return jsonify({
        "selected_regime": regime.title(),
                    "gross": round(gross_income, 2),
                    "taxable_income": round((gross_income - standard_deduction), 2),
                    "total_tax": round(selected_tax, 2),
                    "total_deductions": round(deducations, 2),
                    "tax_before_cess": round(selected_base_tax, 2),
                    "cess": round(selected_extra_cess, 2),
                    "old_regime_tax": round(old_tax, 2),
                    "new_regime_tax": round(new_tax, 2)
                    
                    
                })