n= int(input("enter the number"))
smallest=int(input("enter the number"))
list3=[]
for i in range(n):
    number=int(input("enter the number"))
    list3.append(number)
    if list3[i]<smallest:
        smallest=list3[i]
print(smallest)
