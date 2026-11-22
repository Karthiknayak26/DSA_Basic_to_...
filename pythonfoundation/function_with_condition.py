def find_largest(n):
    largest=0
    for i in range(n):
        number=int(input("enter the number:"))
        if number>largest:
            largest=number
    return largest

n=int(input("enter the n:"))
result=find_largest(n)
print(result)