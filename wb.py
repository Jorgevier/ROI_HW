class Property:
    def __init__(self):
        self.income = float(input('How much rent do you collect? '))
        self.expense = float(input('What are your monthly expenses? '))
        self.downPayment = float(input('How much was the down payment? '))
        self.closingCosts = float(input('What were the closing costs? '))
        self.rehab = float(input('How much to fix it? '))
    def yearlyCashFlow(self):
        return (self.income - self.expense) * 12
    def investment(self):
        # downPayment + closingCosts + rehab = total investment
        return self.downPayment + self.closingCosts + self.rehab
    def roi(self):
        # roi = (yearlyCashFlow / investment) * 100
        return (self.yearlyCashFlow() / self.investment()) * 100
# Usage example
property1 = Property()
print(f"Your rate of investment is {property1.roi()}%")