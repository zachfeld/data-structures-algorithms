import random

def quicksortRandom(arr, lowIndex, highIndex):
    if lowIndex < highIndex:
        #sets partition index to the proper partition
        partitionIndex = randomPartition(arr, lowIndex, highIndex)
        #sorts elements before the partition and after the partition
        quicksortRandom(arr, lowIndex, partitionIndex-1)
        quicksortRandom(arr, partitionIndex+1, highIndex)

def randomPartition(arr, lowIndex, highIndex):
    #pick a random pivot index for partitioning
    randomIndex = random.randint(lowIndex, highIndex)
    #set the value at that random index to current lower index
    arr[lowIndex], arr[randomIndex] = arr[randomIndex], arr[lowIndex]
    return partition(arr, lowIndex, highIndex)


def partition(arr, lowIndex, highIndex):
    pivot = arr[highIndex]
    i = lowIndex - 1

    #move through array comparing to pivot
    for j in range(lowIndex, highIndex):
        #if current element is smaller than pivot
        if arr[j] < pivot:
            #index of smaller ele moves up
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[highIndex] = arr[highIndex], arr[i+1]
    return (i + 1)


arr = [10, 2, 1, 5, 3, 6, 9, 8]
quicksortRandom(arr, 0, len(arr) - 1)

print(arr)