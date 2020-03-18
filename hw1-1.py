name = input("Enter name: ")
age = int(input("Enter age: "))
password = input("Enter password: ")
while len(password) < 6:
    print("Too short password")
    password = input("Enter password: ")
print("Name: ", name)
print("Age: ", age)
print(type(name))
print(type(age))
print(type(password))
#+?