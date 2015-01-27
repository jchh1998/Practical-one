__author__ = 'Jordan'

name = input("Enter Name")
hours = int(input("Enter number of hours worked weekly"))
rate = float(input("Enter hourly rate"))
cpf = float(input("Enter CPF rate in %"))

gross = hours * rate
net = gross * ((100-cpf)/100)
cpf1 = gross * (cpf/100)

print("Payroll for",name)
print("Number of hours worked in week = ",hours)
print("Hourly rate $", rate)
print("Gross pay $",gross)
print("Net pay $",net)
print("CPF contribution $",cpf1)