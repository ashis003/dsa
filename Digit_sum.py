def sum_of_digit(n):
    sum=0
    for ele in n:
        for j in ele:
            temp=j/10
            sum=sum+temp
            print(sum)
n=[12,13,14,15,16]
sum_of_digit(n)