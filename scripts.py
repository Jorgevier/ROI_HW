class Property:
    def __init__(self):
        self.income = 0
        self.expense = 0
        self.downPayment = 0
        self.closingCosts = 0
        self.rehab = 0

    def yearlyCashFlow(self):
        return( self.income() -  self.expense()) *12

    def investment(self):
        # downPayment + closingCost + rehab = investment
        return (self.downPayment() + (self.closingCosts() + self.rehab()))

    def roi(self):
        return (self.yearlyCashFlow / self.investment)*100

    income = input('how much rent you collect? ')
    expense = input('whats your monthly expense? ')
    downPayment = input('how much down payments you put? ')
    closingCosts = input('whats the closing cost? ')
    rehab = input('how much to fix it? ')

Property   



# print (f"your rate of investment is '{Property.roi}'%")
# input rent income?
# p=Property('2000','1610','40000','3000','7000')




# p.
# # input total exp?
# p.
# # input down payment
# p.
# # input closing cost
# p.
# # input rehab
# p.
# print ('you rate of intrest is', (p.roi), '%' )
# Property()


