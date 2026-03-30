def calculate_net_tax(total_income:float):
    taxable_income = total_income - 75000
    print(taxable_income)
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
        slab_tax = ((taxable_income - 400000) * 0.10) 
        base_tax = slab_tax
    elif taxable_income > 300001:
        base_tax = 0
        

    extra_cess = base_tax * 0.04
    print(extra_cess)
    net_payable_tax = base_tax + extra_cess
    return round(net_payable_tax,2)
    
if __name__ == "__main__":
    tax = calculate_net_tax((eval(input())))
    print(tax)