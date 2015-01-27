__author__ = 'Jordan'

print ("Welcome to Jordan's Mile to KM converter!")

km = float(input("Please enter miles to be converted into Kilometer"))
m = round((km*1.60934),2)

if type(km) == float:
    print ("Your input in KM is" ,m)
