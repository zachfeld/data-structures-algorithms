# A python program for finding the largest sum in an array of values

def maxSubarray(arr):
    #working set of variables and finalized set of variables
    currentMax = float('-inf')
    startIndex = 0
    endIndex = 0
    maxStart = 0
    maxEnd = 0
    workingMax = float('-inf')

    for i in range (len(arr)):
        #if the current array position is better than the next one added
        #set the index to where you currently are
        if(arr[i] > arr[i] + workingMax):
            workingMax = arr[i]
            startIndex = i
            endIndex = i
        else:
            #append the next value to the working maximum
            workingMax = workingMax + arr[i]
            endIndex = i
        
        #if max that I currently have is better than what I had before
        #turn all variables to what I have now
        if (workingMax > currentMax):
            currentMax = workingMax
            maxStart = startIndex
            maxEnd = endIndex

    print ("Starting index: " + str(maxStart) + " Ending index: " + str(maxEnd))
    print ("The max subarray is: " + str(currentMax) + "\n")

#Test for random number input
arr = [-2, -3, 4, -1, -2, 1, 5, -3]

maxSubarray(arr)

#Test for all positive numbers
arr = [10, 12, 13, 15, 10, 40, 33]

maxSubarray(arr)

#Test for all negative numbers
arr = [-10, -12, -13, -15, -10, -40, -33]

maxSubarray(arr)

#Test for all negative numbers last number should drown them out
arr = [-10, -12, -13, -15, -10, -40, 100]

maxSubarray(arr)