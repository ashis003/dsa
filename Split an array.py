def arrSplit(arr,d):
    for i in range(0,d):
        temp=arr[0]
        for j in range(0,len(arr)-1):
            arr[j]=arr[j+1]
        arr[-1]=temp
def arrPrint(arr):
    for i in range(0,len(arr)):
        print(arr[i],end=" ")
arr=[1,2,3,4,5]
d=2
arrSplit(arr,d)
arrPrint(arr)