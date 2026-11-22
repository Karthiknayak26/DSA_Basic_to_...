def binary_search(arr,low,high,key):
    mid=(low+high)/2
    for i in range(len(arr)):
        if arr[i]==key:
            return i
        elif arr[i]<mid:
            high=mid-1
        else:
            low=mid+1
    return -1

arr=[20,40,50,60,70]
key=80
n=len(arr)
low=arr[0]
high=arr[n-1]
result=binary_search(arr,low,high,key)
if result==-1:
    print("not found")
else:
    print("found")