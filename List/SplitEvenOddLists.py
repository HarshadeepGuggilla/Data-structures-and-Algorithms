#Split even and odd elements from mix list
def evenOddLists(lst):
    even_lst = []
    odd_lst = []
    for i in range(len(lst)):
        if lst[i]%2==0:
            even_lst.append(lst[i])
        else:
            odd_lst.append(lst[i])
    print(even_lst)
    print(odd_lst)
    
def split(lst):
    even_lst = []
    odd_lst = []
    for i in lst:
        if i%2==0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
    print(even_lst)
    print(odd_lst)
    
lst = [2, 5, 13, 17, 51, 62, 73, 84, 95]
evenOddLists(lst)
split(lst)