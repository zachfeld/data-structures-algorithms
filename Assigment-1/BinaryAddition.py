# A program to add two n bit binary integers stored in n element arrays

def binaryAddition(a, b):

    #first passthrough will never have carry over
    carryOver = False

    # create n + 1 element array
    c = [0] * (len(a) + 1)

    #Loop from end of a and b to the beginning of c (len(a) to -1)
    for i in range(len(a) - 1, -2, -1):
        # beginning of c, check if you need preceeding 1
        if (i == -1):
            if (carryOver == True):
                c[i + 1] = 1 
        # if both elements are one, check if carry over is present
        elif (a[i] == 1 and b[i] == 1):
            if (carryOver == False):
                carryOver = True
                c[i + 1] = 0
                print(c)
            else:
                c[i + 1] = 1
                print(c)
        # if one element is one and the other is 0, check if carry over is present
        elif (a[i] == 1 and b[i] == 0 or b[i] == 1 and a[i] == 0):
            if (carryOver == True):
                c[i + 1] = 0
            else:
                c[i + 1] = 1
            print(c)
        # if both elements are zero, check if carry over is present
        elif (a[i] == 0 and b[i] == 0):
            if (carryOver == True):
                c[i + 1] = 1
                carryOver = False
        # default case, check if needed
        else:
            c[i + 1] = 0
            print(c)
            
    return c


arr1 = [1, 0, 1, 1, 1, 0, 1]
arr2 = [1, 0 ,1, 0, 1, 1, 0]

c = binaryAddition(arr1, arr2)


print(c)