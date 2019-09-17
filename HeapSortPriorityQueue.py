#A traditional heapsort algorithm that also implements the methods of a priority queue

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

#given a child index, returns parent index of the heap
def getParentIndex(childIndex):
    parentIndex = (childIndex - 1) / 2
    return parentIndex

# inserts a value into the heap
def insert(arr, value):
    #put a really small value into the end of the heap
    arr.append(float('-inf'))
    #put that value where it needs to be, using the increase key
    increaseKey(arr, len(arr), value)

#returns the element with the highest value
def maximum(arr):
    buildMaxHeap(arr)
    return arr[0]

#removes and returns the element with the highest value from the heap
def extractMax(arr):
    #make sure that the array maintains the max heap property
    buildMaxHeap(arr)
    #don't want to eliminate the last element, so if there is only one element do nothing
    if len(arr) < 1:
        return
    else:
        max = arr[0]
        #move a value to the place of the extracted value
        arr[0] = arr[len(arr)-1]
        #remove the last element in the heap
        arr.pop()
        #maintain the max heap property
        maxHeapify(arr, len(arr), 0)
        return max

#incereases the value of element x's key to the new value k
#which is assumed to be at least as large as x already is
def increaseKey(arr, index, value):
    if value < arr[index]:
        return #new value is smaller than current value at given index
    a[index] = value
    while (index > 1 and arr[getParentIndex(index)] < arr[index]):
        #swap parent with child
        arr[index], arr[getParentIndex(index)] = arr[getParentIndex(index)], arr[index]
        #move index up to the parent index
        index = getParentIndex(index)



arr = [7, 11, 12, 14, 15, 7, 8, 1]

extractMax(arr)

print(arr)