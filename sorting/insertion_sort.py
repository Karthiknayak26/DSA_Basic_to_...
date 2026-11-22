def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        key=arr[i]
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key 
    return arr
arr=[3,5,6,8,3]
print(insertion_sort(arr))   
