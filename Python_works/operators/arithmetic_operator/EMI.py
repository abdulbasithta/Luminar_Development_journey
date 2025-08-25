# EMI
"""

EMI = p*r* (1+r)^n /(1+r)^n-1

p = loan_amount
r = monthly intrest rate (annual_rate / (12*100))
n = loan tenure in month (year*12)

"""

# Loan Amount

loan_amount = int(input("Enter the Loan Amount: "))

# Intrest of Loan in percentage

intrest_rate = int(input("Enetr Intrest Rate: "))

# loan tenure (year)

loan_tenure = int(input("Enter tenure: "))

p = loan_amount

r = intrest_rate / (12*100)

n = loan_tenure * 12

EMI = (p * r * (1 + r)** n) / ((1 + r)** n - 1)

print("Monthly EMI", round(EMI , 2))

# Total payable Amount

tot_pay_amount = EMI * n

print("Total Amount", round(tot_pay_amount, 2))

# Total intrest amount

tot_intrest = tot_pay_amount - p

print("Total intrest", round(tot_intrest, 2))

# value = 12045.5633

# print(round(value,1))