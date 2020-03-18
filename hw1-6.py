x = int(input("Enter values of day 1: "))
y = int(input("Enter target: "))
day = 1
while y - x > 0:
    x = x + (x * 0.1)
    day += 1
print("Result will be achieved on the day:", day)
#+?