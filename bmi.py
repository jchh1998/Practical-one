__author__ = 'dhs'
weight = input("Please enter your weight")
height = input("Please enter your height")

w = float(weight)
h = float(height)

bmi = round(w/(h*h),5)

print("Your BMI is", bmi)

if bmi <= 18.5:
    print("You're underweight please eat more")
if 18.5 < bmi < 24.9:
    print("Your Weight and height go well together!")
if bmi >= 25.0:
    print("Something needs to be done about your weight!")