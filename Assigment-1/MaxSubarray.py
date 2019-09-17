# A python program for finding the largest sum in an array of values

def maxSubarray(arr):

    #make current max a really small number
    currentMax = -20000000000
    workingMax = 0

    for i in range (0, len(arr)):
        # increase max by each element of the array per instance of the loop
        workingMax = workingMax + arr[i]
        # if the built array is bigger than what is currently identified as the biggest max
        # change the current max to what you have been building
        if (currentMax < workingMax):
            currentMax = workingMax
        # if max you have been building needs a reset, reset it
        if workingMax < 0:
            workingMax = 0
    return currentMax



arr = [-2, -3, 4, -1, -2, 1, 5, -3]

print("the max subarray is",  maxSubarray(arr))