#insertion sort ascending order
def insertionSort(arr):
    arr=[5,2,17,3,4,9,15,1]
    for i in range(1,len(arr)):
        current=arr[i]
        pos=i
        while current<arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1
            arr[pos]=current
if __name__ == "__main__":
    arr = [5,2,17,3,4,9,15,1]
    insertionSort(arr)
    print(*arr)
    
    