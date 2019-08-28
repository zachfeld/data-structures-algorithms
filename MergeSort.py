def mergeSort(arr):
    if len(arr) > 1:
        #middle of array and split into two seperate arrays for L and R
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        #recurse until 1 element left and sort
        mergeSort(L) 
        mergeSort(R)

        #set all pointers to zero
        i = j = k = 0

        #copy data into temporary arrays of L and R
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        #check if any element left behind
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1


arr = [12, 11, 13, 5, 7, 6, 11, 12, 15, 67, 80, 1]

mergeSort(arr)

print(arr)