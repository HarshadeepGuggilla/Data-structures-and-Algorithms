def reverseNumber(n: int):
    temp=n
    rev=0
    while temp>0:
        digits=temp%10
        rev=(rev*10)+digits
        temp=temp//10
    return rev

n=int(input("Enter a number to check if it palindrome or not"))
if n==reverseNumber(n):
    print("Palindrome", n, " ", reverseNumber(n))
else:
    print("Not a palindrome", n, " ", reverseNumber(n))