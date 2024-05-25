print("Finding Factorial of a Number")
def factorial (n):
    if (n==1 or n==0):
        return 1
    else:
        return n* factorial(n-1) #recursion
n= int(input("Enter a Number = "))
print("Factorial of",n,"is",factorial(n))