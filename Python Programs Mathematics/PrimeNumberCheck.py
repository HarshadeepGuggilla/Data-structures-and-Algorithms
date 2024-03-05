def isPrimeNumber(n: int):
    for i in range(2, n):
        if n%i == 0:
            return 1
    return 0
    
n=int(input("Enter a number"))    
if isPrimeNumber(n)==0:
    print("Prime number")
else:
    print("Not a prime number")
    
            