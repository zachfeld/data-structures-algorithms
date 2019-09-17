# this function maintains the min heap property of a given node in an array
def minHeapify(arr, heapSize, parentIndex):

    smallestIndex = parentIndex #initialize smallest as root
    leftIndex = (2 * parentIndex) + 1 #left index equation
    rightIndex = (2 * parentIndex) + 2 #right index equation

    #check if left of root node exists and if it is smaller than parent
    if (leftIndex < heapSize and arr[leftIndex] < arr[parentIndex]):
        smallestIndex = leftIndex

    #check if right of root node exists and if it smaller than the current smallest
    if (rightIndex < heapSize and arr[rightIndex] < arr[smallestIndex]):
        smallestIndex = rightIndex

    #change the value of the root if we made a switch
    if (smallestIndex != parentIndex):
        arr[parentIndex], arr[smallestIndex] = arr[smallestIndex], arr[parentIndex]

        #recurse into the root of the switched node
        minHeapify(arr, heapSize, smallestIndex)

#loop through array and maintain the min heap property
def buildMinHeap(arr):
    heapSize = len(arr)
    for index in range (heapSize, -1, -1):
        minHeapify(arr, heapSize, index)

def heapSortMin(arr):

    #build min heap based on passed array
    buildMinHeap(arr)

    heapSize = len(arr)

    #loop through the array, switching the root node to the end
    #as it bubbles to the top through the minHeapify method
    for index in range (heapSize - 1, 0, -1):
        arr[0], arr[index] = arr[index], arr[0]

        minHeapify(arr, index, 0)


arr = [7, 11, 12, 14, 15, 7, 8, 1]

heapSortMin(arr)

print(arr)