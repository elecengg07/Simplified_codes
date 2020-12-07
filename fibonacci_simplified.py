# Fibonacci Series

"""Decalre an empty list"""
fib = [0,1]

"""Take input from user"""
n = int(input("Enter any integer value greater than 1:"))
# x = 0

"""conditional statements"""
if n<=0:
    print("wrong number")
elif n==1:
    print(fib[0])
elif n==2:
    print(fib[1])
else:
    for i in range(2,n+1):
        x =  fib[i-1]+fib[i-2]
        fib.append(x)
    print(fib)
    print(fib[n-1])