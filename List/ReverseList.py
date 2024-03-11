#Reverse a list using two pointer approach swap method

def reverseList(lst):
    s=0
    e=len(lst)-1
    while s<e:
        lst[s],lst[e] = lst[e],lst[s]
        s=s+1
        e=e-1
    print("Reversed List", lst)

lst = [10,20,30,1,2,3]
reverseList(lst)