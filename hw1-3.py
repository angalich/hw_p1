n = int(input("Enter number n: "))
str_n = str(n)
sums = n
sum_str = str(n)
for i in range (1, 3):
    sum_str = sum_str + str_n
    sums = sums + int(sum_str)
print(sums)
#+