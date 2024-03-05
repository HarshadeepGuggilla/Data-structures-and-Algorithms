# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def gcd(a: int, b: int):
    if a==0:
        return b
    if b==0:
        return a
    if a==b:
        return a
    if a > b:
        return gcd(a-b, a)
    if b > a:
        return gcd(a, b-a)

def gcdSimple(a: int, b: int):
    if b==0:
        return a
    return gcdSimple(b, a%b)

print("GCD or HCF of two numbers is", gcdSimple(28, 21))
print("GCD or HCF of two numbers is", gcd(7, 21))