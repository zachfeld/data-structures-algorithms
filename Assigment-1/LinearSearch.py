import sys

#returns the index of the first instance of an element inside of an array
def linearSearch(arr, v):
    for i in range(len(arr)):
        if (arr[i] == v):
            print(i)
            return True
    print("Item not found in list")
    return False

#test case where the element is in the last position
arr = [5, 2, 4, 6, 1, 7]
linearSearch(arr, 7)

#test case where the element is in the middle
arr = [5, 2, 4, 6, 1, 7]
linearSearch(arr, 4)

#test case where the element is not in the array
arr = [5, 2, 4, 6, 1, 7]
linearSearch(arr, 10)