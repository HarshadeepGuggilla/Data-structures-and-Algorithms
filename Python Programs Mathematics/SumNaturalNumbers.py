# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def sumNaturalUsingLoop(n: int):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
    
def sumNaturalNumbers(n: int):
    if n==0:
        return 0
    sum=n*(n+1)/2
    return sum
    
#Input    
n=int(input("Enter a number"))     

#sum of natural Numbers using mathematical formula
print("Sum of natural numbers using mathematical formula", sumNaturalNumbers(n))

#sum of natural numbers using naive method
print("Sum of natural numbers using naive method", sumNaturalUsingLoop(n))
