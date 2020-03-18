number = int(input("Enter number >0: "))
t = 0
while number > 0:
    i = number % 10
    number //= 10
    if i > t:
        t = i
print(t)
#+