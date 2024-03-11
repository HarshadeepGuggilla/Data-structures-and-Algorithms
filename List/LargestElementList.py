#largest element in list

def largestElement(lst):
    large=lst[0]
    for i in lst:
        if i > large:
            large=i
    return large

lst=[1,2,43,2,3,98,0,12]
print("Largest element in list ", largestElement(lst))