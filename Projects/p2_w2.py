# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 14:34:04 2019

@author: VIJ Global
"""
balance = int(input("please put your balance on your credit card: "))
annualInterestRate = float(input("please put your annual interest rate in decimal: "))

monthlyInterestRate = annualInterestRate/12
i = 0
month = 0
monthlyPaymentLower = int (round((balance/12),-1))
monthlyPaymentUpper = int (round(((balance*(1+monthlyInterestRate)**12)/12.0),-1))
amount = int(round(((monthlyPaymentLower+monthlyPaymentUpper)/2),-1))
diff = 0.01
while abs(amount-balance) >= diff:
    
    if amount < balance and i < 12:
        monthlyPaymentUpper = amount
        i += 1
        print("month: ", month, "amount: ",amount)
    else:
        break  
    month += 1
amount = int(round (amount,-1))
print ("Lowest Payment: ", amount, "after ", month, " months")


"""___Real code without bisection___
monthlyPaymentRate = 0
init_balance = balance
monthlyInterestRate = annualInterestRate/12

while balance > 0:
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > 0:
        monthlyPaymentRate += 10
        balance = init_balance
    elif balance <= 0:
        break
print('Lowest Payment:', monthlyPaymentRate)
"""