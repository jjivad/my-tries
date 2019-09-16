# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:57:09 2019

@author: VIJ Global
"""


balance = int(input("please put your balance on your credit card: "))
annualInterestRate = float(input("please put your annual interest rate in decimal: "))

monthlyInterestRate = annualInterestRate/12
i = 0
month = 0
diff = 0.01

monthlyPaymentLower = balance/12
monthlyPaymentUpper = (balance*(1 + monthlyInterestRate)**12)/12.0
amount= 0
unit_balance = balance
while abs(amount-balance) >= diff:
    balance = balance - amount + ((balance - amount) * monthlyInterestRate)
    if balance != 0 and i < 12:
        amount = (monthlyPaymentLower+monthlyPaymentUpper)/2
        i += 1
        print("month: ", month, "amount: ",amount, "my balance is: ", balance)
    else:
        break  
    month += 1
amount = round (amount,2)
print ("Lowest Payment: ", amount, "after ", month, " months")



"""___Real code without bisection___
amount = 0
init_balance = balance
monthlyInterestRate = annualInterestRate/12

while balance > 0:
    for i in range(12):
        balance = balance - amount + ((balance - amount) * monthlyInterestRate)
    if balance > 0:
        amount += 10
        balance = init_balance
    elif balance <= 0:
        break
print('Lowest Payment:', amount)
"""




"""___Real code without bisection___

balance = int(input("please put your balance on your credit card: "))
annualInterestRate = float(input("please put your annual interest rate in decimal: "))

monthlyInterestRate = annualInterestRate/12

monthlyPaymentLower = balance/12
monthlyPaymentUpper = (balance*(1+monthlyInterestRate)**12)/12.0
amount = (monthlyPaymentLower+monthlyPaymentUpper)/2


init_balance = balance
diff = 0.01

while abs(amount-balance) >= diff:
    for i in range(12):
        balance = balance - amount + ((balance - amount) * monthlyInterestRate)
        print (amount)
    if balance > 0:
        amount += 10
        balance = init_balance
    elif balance <= 0:
        break
amount = round (amount,2)
print('Lowest Payment:', amount)
"""