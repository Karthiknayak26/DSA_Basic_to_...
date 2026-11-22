n=int(input("enter the number"))
list2=[]
sum=0
largest=int(input("enter the number"))
for i in range(n):
    number=int(input("enter the number"))
    list2.append(number)
    if list2[i]>largest:
        largest=list2[i]
    sum=sum+list2[i]
print(largest)
print(sum)



