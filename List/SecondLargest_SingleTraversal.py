#Second largest ---All test cases Single traversal
def secondLargest(lst):
    if len(lst) <=1:
        return None
    lar=lst[0]
    slar=None
    for i in range(1, len(lst)+1):
        if i>lar:
            lar=i
            slar=lar
        elif i!=lar:
            if slar<i or slar==None:
                slar=i
    return slar
    
lst=[20,20,10,12, 45, 21]
print("Second largest element in list is", secondLargest(lst))