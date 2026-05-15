#ascending order
# def selectionSort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]

# if __name__ == "__main__":
#     arr = [6, 23, 2, 4, 1, 8, 56, 3]
#     selectionSort(arr)
#     print(*arr)

#descending order
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

if __name__ == "__main__":
    arr = [6, 23, 2, 4, 1, 8, 56, 3]
    selectionSort(arr)
    print(*arr)