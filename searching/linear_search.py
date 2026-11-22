def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1

arr=[20,40,5,10]
key=5
result =linear_search(arr,key)
if result==-1:
    print("element is found")
else:
    print("not found")
    