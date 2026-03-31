def calculate_net_tax(total_income: float, regime: str, deductions=0) -> float:
    """Tax calculation based on the new or old regime"""
    try:
        if total_income is None :
            return "Please enter a valid total income."
        
        if regime == "new":
           base_tax = new_regime_tax_calculation()
        else:
            standard_deduction = 50000
            taxable_income = float(total_income) - standard_deduction - deductions
            print(taxable_income)
            if 1000001 <= taxable_income :
                slab_tax = (taxable_income - 1000000) * 0.3
                base_tax = slab_tax + 112500
            elif 500001 <= taxable_income <= 1000000:
                slab_tax = ((taxable_income - 500000) * 0.20) 
                base_tax = slab_tax + 12500
            elif 250001 <= taxable_income <= 500000:
                slab_tax = ((taxable_income - 250000) * 0.05) 
                base_tax = slab_tax
            elif taxable_income <= 250000:
                base_tax = 0
        
        extra_cess = 0        
        if base_tax >= 1:
            extra_cess = round((base_tax * 0.04),2)
            print(extra_cess)
        net_payable_tax = base_tax + extra_cess
        tax = round(net_payable_tax,2)
        return tax
    except Exception as e:
        return ValueError(f"An error occured {str(e)}")
    
def total_deductions(d80c: float, d80d: float, hra: float, hl: float, nps:float):
    net_deductions = d80c + d80d + hra + hl + nps
    return net_deductions

def new_regime_tax_calculation(total_income: float, deductions=0):
    standard_deduction = 75000
    taxable_income = float(total_income) - standard_deduction - float(deductions)    
    if 2400001 <= taxable_income :
        slab_tax = (taxable_income - 2400000) * 0.3
        base_tax = slab_tax + 300000
    elif 2000001 <= taxable_income <= 2400000:
        slab_tax = ((taxable_income - 2000000) * 0.25)
        base_tax = slab_tax + 200000
    elif 1600001 <= taxable_income <= 2000000:
        slab_tax = ((taxable_income - 1600000) * 0.20) 
        base_tax = slab_tax + 120000
    elif 1200001 <= taxable_income <= 1600000:
        slab_tax = ((taxable_income - 1200000) * 0.15) 
        base_tax = slab_tax + 60000
    elif 800001 <= taxable_income <= 1200000:
        slab_tax = ((taxable_income - 800000) * 0.10) 
        base_tax = slab_tax + 20000
    elif 400001 <= taxable_income <= 800000:
        slab_tax = ((taxable_income - 400000) * 0.05) 
        base_tax = slab_tax
    elif taxable_income <= 400000:
        base_tax = 0
    
    return base_tax

