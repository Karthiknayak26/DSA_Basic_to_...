def find_sum(n):
    sum=0
    for i in range(n):
        number=int(input("enter the number:"))
        sum=sum+number

    return sum

n=int(input("enter the n"))
# find_sum(n)
result=find_sum(n)
print(result)