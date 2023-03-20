import array as arr
arr = arr.array("i",[11,2,3,4,5])
for i in range(0,4):
    arr.reverse()
    for j in range(4,len(arr)):
        arr.reverse()
        for k in range(0,len(arr)):
            arr.reverse()
for x in range(0,len(arr)):
    print(arr[x])
    print("hello")