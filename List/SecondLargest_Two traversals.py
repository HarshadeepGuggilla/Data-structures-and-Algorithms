#Second largest ---All test cases Two traversals
def largest(lst):
    lar=lst[0]
    for i in lst:
        lar=max(i, lar)
    return lar
    
def secondLargest(lst, lar):
    slar=None
    for i in lst:
        if i!=lar:
            if slar==None:
                slar=i
            else:
                slar=max(slar, i)
    return slar
    
lst=[20,20]
lar=largest(lst)
print("largest element in list is", largest(lst))
print("Second largest element in list is", secondLargest(lst, lar))