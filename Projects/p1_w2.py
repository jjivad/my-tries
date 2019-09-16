# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 13:01:07 2019

@author: VIJ Global
"""

balance = int(input("please put your balance on your credit card: "))
annualInterestRate = float(input("please put your annual interest rate in decimal: "))
monthlyPaymentRate = float(input("please put your monthly payment rate in decimal: "))

monthlyInterestRate = annualInterestRate/12.0
i = 0
month = 0

while i < 12:
    month += 1
    monthlyPayment = monthlyPaymentRate * balance
    balance = balance - monthlyPayment
    balance = balance + (balance * monthlyInterestRate)
    i = i + 1

balance = round (balance, 2)    
print ("Remaining balance: ", balance, "after ", month, " months")