import sys
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

#given a child index, returns parent index of the heap
def getParentIndex(childIndex):
    parentIndex = (childIndex - 1) // 2
    return parentIndex

# inserts a value into the heap
def insert(arr, value):
    #put a really large value into the end of the heap
    arr.append(float('inf'))
    #put that value where it needs to be, using the decrease key
    decreaseKey(arr, len(arr), value)

#returns the element with the highest value
def minimum(arr):
    buildMinHeap(arr)
    return arr[0]

#removes and returns the element with the highest value from the heap
def extractMin(arr):
    #make sure that the array maintains the min heap property
    buildMinHeap(arr)
    #don't want to eliminate the last element, so if there is only one element do nothing
    if len(arr) < 1:
        exit()
    else:
        min = arr[0]
        #move a value to the place of the extracted value
        arr[0] = arr[len(arr)-1]
        #remove the last element in the heap
        arr.pop()
        #maintain the min heap property
        minHeapify(arr, len(arr), 0)
        return min

#decreases the value of position index to the new value
#which is assumed to be at least as small as x already is
def decreaseKey(arr, index, value):
    if value > arr[index]:
        exit() #new value is larger than current value at given index
    arr[index] = value
    while (index > 0 and arr[getParentIndex(index)] > arr[index]):
        #swap parent with child
        arr[index], arr[getParentIndex(index)] = arr[getParentIndex(index)], arr[index]
        #move index up to the parent index
        index = getParentIndex(index)

arr = [7, 11, 12, 14, 15, 7, 8, 1]

heapSortMin(arr)

print(arr)