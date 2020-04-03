#  Take input from User and generate fabonnaci series

x = int(input("Please enter your number :  - "))

#  Define initial 2 values
a = 0
b = 1
print(a)
print(b)
while ((a + b) < x):
    b = a + b
    a = b - a
    print(b)
