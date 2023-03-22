def swapList(a):
    for i in range(0,len(a)):
        temp = a[0]
        a[0] = a[-1]
        a[-1] = temp
    print(a)

a=[1,2,3,4,5]
swapList(a)

