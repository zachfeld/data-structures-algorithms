import random

def quicksortRandom(arr, lowIndex, highIndex):
    if lowIndex < highIndex:
        #sets partition index to the proper partition
        partitionIndex = partition(arr, lowIndex, highIndex)
        #sorts elements before the partition and after the partition
        quicksortRandom(arr, lowIndex, partitionIndex-1)
        quicksortRandom(arr, partitionIndex+1, highIndex)

def medianThreePartition(arr, lowIndex, highIndex):

    #can not do this partition if there are less than 3 elements
    if (abs(highIndex - lowIndex) < 3):
        randomValue = random.choice(arr[lowIndex:highIndex + 1])
        randomIndex = arr.index(randomValue)
        
        return [randomIndex, randomValue]
    
    #pick 3 random pivot indicies
    randomIndexSet = random.sample(range(lowIndex, highIndex), 3)
    #transplant those indicies into the corresponding array values
    randomValueSet = []
    for i in range(0, 3):
        randomValueSet.append(arr[randomIndexSet[i]])
    
    #swap both arrays inconfluence with eachother
    swapInConfluence(randomIndexSet, randomValueSet)

    #choose the random index which should be i = 1
    randomIndex = randomIndexSet[1]
    randomValue = arr[randomIndex]
    
    return [randomIndex, randomValue]

#small 3 value insertion sort while 
#keeping the indicies of the two arrays together
def swapInConfluence(indexArr, valueArr):
    if (valueArr[1] < valueArr[0]):
        valueArr[0], valueArr[1] = valueArr[1], valueArr[0]
        indexArr[0], indexArr[1] = indexArr[1], indexArr[0]
    if (valueArr[2] < valueArr[1]):
        valueArr[1], valueArr[2] = valueArr[2], valueArr[1]
        indexArr[1], indexArr[2] = indexArr[2], indexArr[1]
        if (valueArr[1] < valueArr[0]):
            valueArr[0], valueArr[1] = valueArr[1], valueArr[0]
            indexArr[0], indexArr[1] = indexArr[1], indexArr[0]

def partition(arr, lowIndex, highIndex):
    pivotList = medianThreePartition(arr, lowIndex, highIndex)
    pivotIndex = pivotList[0]
    pivotValue = pivotList[1]

    arr[pivotIndex], arr[highIndex] = arr[highIndex], arr[pivotIndex]

    i = lowIndex - 1

    #move through array comparing to pivot
    for j in range(lowIndex, highIndex):
        #if current element is smaller than pivot
        if arr[j] <= pivotValue:
            #index of smaller ele moves up
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[highIndex] = arr[highIndex], arr[i+1]
    return (i + 1)


arr = [10, 2, 1, 5, 3, 6, 9, 8]
quicksortRandom(arr, 0, len(arr) - 1)

print(arr)