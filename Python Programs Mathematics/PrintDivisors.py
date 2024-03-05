def printDivisors(n: int):
    i=1
    while i*i <= n:
        if n%i==0:
            if n/i==i:
                print(i, end=" ")
            else:
                print(i, int(n/i), end="  ")
        i=i+1

print("Dvisiors of a number", printDivisors(20)) #Will print the divisors in pairs


            
        
    
            