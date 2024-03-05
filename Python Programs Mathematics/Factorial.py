# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def factorialRecursive(n: int):
    if n==0 or n==1:
        return 1
    else:
        return n*factorialRecursive(n-1)

def factorialLoop(n: int):
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    return fact
    
n=int(input("Enter a number"))
print("Factorial of a number using Recursion", factorialRecursive(n))
print("Factorial of a number using loop method", factorialLoop(n))