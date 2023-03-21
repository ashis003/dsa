def arrMul(arr,n):
    mul=1
    rem=1
    for i in range(0,len(arr)):
        mul=mul*arr[i]
        rem = mul % n
    print("The value of the array multiplication is : ",mul)
    print("The value of the array remainder is",rem)


arr=[100, 10, 5, 25, 35, 14]
#n=11
n=int(input("Enter the value of n : "))
arrMul(arr,n)

