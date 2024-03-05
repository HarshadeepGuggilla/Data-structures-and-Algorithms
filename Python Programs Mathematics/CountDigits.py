def countDigits(number: int):
    count=0
    while number>0:
        number=number//10
        count=count+1
    return count

n=int(input("Enter a input number "))
print("Count of digits in a number is", countDigits(n))