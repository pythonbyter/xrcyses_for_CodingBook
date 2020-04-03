versayiyi = int(input("hangi sayı= "))

factorial = 1

# check if the number is negative, positive or zero
if versayiyi < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif versayiyi == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, versayiyi + 1):
        factorial = factorial * i
    print("The factorial of", versayiyi, "is", factorial)

z = 1

while (versayiyi >= 0):
    z = z * versayiyi
    versayiyi = versayiyi - 1
else:
    if versayiyi < 0:
        print("negatif")
print("Factorial result is : " + str(z))



