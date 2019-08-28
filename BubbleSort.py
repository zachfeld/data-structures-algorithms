
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range (0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                


array = [5, 2, 4, 6, 1, 3]

bubbleSort(array)

print(array)
