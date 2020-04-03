#good algorithm but the proces is too slow!!


x = int(input("Please enter number of terms for fibosh: "))

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


# check if the number of terms is valid
if x <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(x):
       print(recur_fibo(i))