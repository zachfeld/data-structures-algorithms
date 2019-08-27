# A tradtional insertion sort algorithm with time complexity of n^2
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


array = [5, 2, 4, 6, 1, 3]

insertionSort(array)

print(array)
