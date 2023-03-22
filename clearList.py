n=int(input("Enter the size of list : "))
list=[]
print("Enter the element to insert in a list : ")
for i in range(0,n):
    element=int(input())
    list.append(element)
print("Element present in a list : ",list)
list.clear()
print("List after clearing : ",list)