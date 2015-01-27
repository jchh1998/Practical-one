__author__ = 'Jordan'

totaldigit = int(input("Enter the number you want to be summed up in integer form only between 0-1000!"))

x = totaldigit
if 0 < x < 1000:
    sum1 = (x % 10) + ((x // 10) % 10) + (x // 100)
    print("The Sum is",sum1)
else:
    print("INVALID INPUT")