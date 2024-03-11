#Get smaller elements than x
def getSmallerElements(lst, x):
    smaller_elements=[]
    for i in range(len(lst)):
        if lst[i] < x:
            smaller_elements.append(lst[i])
    print("List with elements smaller than x", smaller_elements)

lst = [1, 12, 4, 25, 8, 10, 11]
x=25
getSmallerElements(lst, x)      
    