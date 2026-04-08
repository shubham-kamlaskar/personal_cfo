class TaxEngine:
    def calculate_net_tax(self, total_income: float, regime: str, deductions: float) -> float | str:
        """Tax calculation based on the new or old regime"""
        try:
            base_tax = 0
            net_tax = 0
            extra_cess = 0
            if total_income is None :
                return "Please enter a valid total income."
            
            if regime == "new":
                base_tax, extra_cess, net_tax = self.new_regime_tax_calculation(total_income)
            else:
                base_tax, extra_cess, net_tax = self.old_regime_tax_calculation(total_income, deductions)
                    
            return base_tax, extra_cess, net_tax
        except Exception as e:
            print(f"An error occured in calculate_net_tax functions {str(e)}")
            raise ValueError(f"An error occurred: {str(e)}")
        
    def total_deductions(self, d80c: float, d80d: float, hra: float, hl: float, nps:float) -> float:
        net_deductions = d80c + d80d + hra + hl + nps
        return net_deductions

    def new_regime_tax_calculation(self, total_income: float):
        base_tax = 0
        standard_deduction = 75000
        taxable_income = float(total_income) - standard_deduction
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
            
        if base_tax >= 1:
            extra_cess = round((base_tax * 0.04),2)
            print(extra_cess)
        net_payable_tax = base_tax + extra_cess
        net_tax = round(net_payable_tax,2)
        
        return base_tax, extra_cess, net_tax

    def old_regime_tax_calculation(self, total_income: float, deductions: float):
        base_tax = 0
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
            
        if base_tax >= 1:
            extra_cess = round((base_tax * 0.04),2)
            print(extra_cess)
        net_payable_tax = base_tax + extra_cess
        net_tax = round(net_payable_tax,2)
        
        return base_tax, extra_cess, net_tax

