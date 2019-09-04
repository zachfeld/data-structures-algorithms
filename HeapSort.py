def maxHeapify(arr, heapSize, parentIndex):

    largestIndex = parentIndex #initializa largest as root
    leftIndex = (2 * parentIndex) + 1 #left index equation
    rightIndex = (2 * parentIndex) + 2 #right index equation

    #check if left child of root node exists and if it is greater than root
    if (leftIndex < heapSize and arr[leftIndex] > arr[parentIndex]):
        largestIndex = leftIndex

    #check if right child of root node exists and if it is greater than root
    if (rightIndex < heapSize and arr[rightIndex] > arr[largestIndex]):
        largestIndex = rightIndex

    #change the root if we made a switch
    if (largestIndex != parentIndex):
        arr[parentIndex], arr[largestIndex] = arr[largestIndex], arr[parentIndex]

        #recurse into the root of the switched node
        maxHeapify(arr, heapSize, largestIndex)

#loop through array and maintain the max heap property
def buildMaxHeap(arr):
    heapSize = len(arr)
    for index in range (heapSize, -1, -1):
        maxHeapify(arr, heapSize, index)

def heapSort(arr):

    #build a max heap based on the passed array
    buildMaxHeap(arr)
    
    heapSize = len(arr)

    #loop through the array, switching the root node to the end 
    #as it bubbles to the top through the maxHeapify method
    for index in range (heapSize - 1, 0, -1):
        arr[0], arr[index] = arr[index], arr[0]
        
        maxHeapify(arr, index, 0)


arr = [7, 11, 12, 14, 15, 7, 8, 1]

buildMaxHeap(arr)

print(arr)