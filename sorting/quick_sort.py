def quick_sort(arr,low,high):
    if low<high:
        pi=partion(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

def partion(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i =i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]

    return i+1

arr=[1,2,3,4,5]
quick_sort(arr, 0, len(arr)-1)
print("Sorted array:", arr)