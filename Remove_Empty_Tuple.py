def remove_tuples(n):
    print("The list before removal of tuples : ",n)
    x={}
    for i in n:
        if i==x:
            n.remove(i)
    print("The list after removing of tuples : ",n)
n=[1,2,{},5,4,{},9,44,54,{}]
remove_tuples(n)
