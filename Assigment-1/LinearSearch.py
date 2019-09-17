def linearSearch(arr, v):
    for i in range (0, len(arr)):
        if (arr[i] == v):
            print(i)
        elif (i == len(arr) - 1):
            print("value not found in sequence")


arr = [5, 2, 4, 6, 1, 7]

linearSearch(arr, 7)