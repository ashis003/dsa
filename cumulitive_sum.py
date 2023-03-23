def cumulitive_sum(n):
    sum=0
    print("The cumulitive sum of the list : ")
    for i in n:
        sum=sum+i
        print(sum,end=" ")
n=[10,20,30,40,50]
cumulitive_sum(n)