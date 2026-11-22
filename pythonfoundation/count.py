ecount=0
ocount=0
n=int(input("enter the n:"))
for i in range(0,n):
    numbers=int(input("enter the number:"))
    if(numbers %2==0):
        ecount+=1
    else:
        ocount+=1
print(ecount)
print(ocount)
        
