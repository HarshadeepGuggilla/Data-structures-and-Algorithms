#Second largest element in a List ---Not working for negative numbers and 0 
def largest(lst):
    lar=lst[0]
    for i in lst:
        if i>lar:
            lar=i
    return lar

def secondLargest(lst, lar):
    slar=0
    for i in lst:
        if i>slar and i!=lar:
            slar=i
    if slar!=0:
        return slar
    else:
        return None

lst=[20, 21, 21, 22, 23, 23, 24, 24, 98, 77]
#lst=[-1,-2, 0]
lar=largest(lst)
slar=secondLargest(lst, lar)
print("Largest element", lar)
print("Second largest", slar)