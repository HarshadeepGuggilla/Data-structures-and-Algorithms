#Left rotate array by one - Single traversal
def leftRotatelist(lst):
    first=lst[0]
    for i in range(1,len(lst)):
        lst[i-1]=lst[i]
    lst[len(lst)-1]=first
    return lst
    
lst=[10,20,21,22,23,24]
print("Left rotated list by one", leftRotatelist(lst))