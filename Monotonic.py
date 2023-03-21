def arrMonotonic(arr):
    return (all(arr[i]>= arr[i+1] for i in range(0,len(arr)-1) or
                all(arr[i]<=arr[i+1] for i in range(0,len(arr)-1))))


arr=[1,2,3,4,5]
print(arrMonotonic(arr))