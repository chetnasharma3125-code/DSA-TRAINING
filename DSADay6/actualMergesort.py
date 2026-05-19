#the idea of merge sort  is 

#divide the list into smaller part
#sort each smaller part
#Merge them back together

# Ddivide the list into smaller parts(unsorted list)
# Sort each smaller part
# Merge them back together
  
class MergeSorts:

    def mergeSort(self, arr):
      if len(arr) > 1:
        mid = len(arr) // 2
        arr1 = arr[:mid]
        arr2 = arr[mid:]
        self.mergeSort(arr1)
        self.mergeSort(arr2)

        i = 0
        j = 0
        k = 0

        while i < len(arr1) and j < len(arr2):

            if arr1[i] < arr2[j]:
                arr[k] = arr1[i]
                i += 1
                k += 1
            else:
                arr[k] = arr2[j]
                j += 1
                k += 1

        while len(arr1) > i:
            arr[k] = arr1[i]
            i += 1
            k += 1

        while len(arr2) > j:
            arr[k] = arr2[j]
            k += 1
            j += 1

        return arr


if __name__ == "__main__":

    obj = MergeSorts()

    arr1 = [8, 4, 67, 78, 10, 5]  
    ans = obj.mergeSort(arr1)
    print(arr1)