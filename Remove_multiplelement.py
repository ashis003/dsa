
#def remove_Multiple(n):
#   print("The element present in the list is : ",n)
#   del n[1:5]
#    print("The element present in the list after removal ",n)
#n=[1,2,3,4,5,6]
#remove_Multiple(n)

# Alternative method
def remove_multiple(n):
    print("Element present in the list before removal : ",n)
    for i in n:
        if i % 2 == 0:
            n.remove(i)
    print("Element present in the list after removal : ", n)
n=[1,2,3,4,5,6]
remove_multiple(n)


