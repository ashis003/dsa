def arrRotate(arr,start,end):
    while(start<end):
        temp = arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1
def leftRotate(arr,d):
    arrRotate(arr,0,d-1)
    arrRotate(arr,d,len(arr)-1)
    arrRotate(arr,0,len(arr)-1)
def printArray(arr):
    for i in range(0,len(arr)):
        print(arr[i],end=" ")
arr=[1,2,3,4,5]
d=2
leftRotate(arr,d)
printArray(arr)
