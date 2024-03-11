#Check if a list is sorted or not
def isSorted(lst):
    n=len(lst)
    if n==0 or n==1:
        print("No elements or single element found in list")
    for i in range(1, n):
        if lst[i] < lst[i-1]:
            print(lst[i], " ", lst[i-1])
            return True
    return False
        
    
lst = [10,20,30,15,40]
if isSorted(lst):
    print("Not sorted")
else:
    print("Sorted")

