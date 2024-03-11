#Average or Mean of a List
def mean(lst):
    return sum(lst)/len(lst)

def sumNaive(lst):
    sum=0
    for i in range(len(lst)):
        sum=sum+lst[i]
    return sum

lst = [15, 9, 55, 41, 35, 20, 62, 49]
print("Average of a list using simple method", mean(lst))
print("Average of a list using naive looping  method", sumNaive(lst)/len(lst))

