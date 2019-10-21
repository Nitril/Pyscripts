

def findlowest(inputarray):
    lowestindex = 0;
    for index in range(1,len(inputarray)):
        if inputarray[index][1] < inputarray[lowestindex][1]:
            lowestindex = index
    return lowestindex

def sort(inputarray):
    outputarray = []

    for index in range(len(inputarray)):
        lowestindex = findlowest(inputarray)
        outputarray.append(inputarray.pop(lowestindex))

    return outputarray


print(sort([(4,2), (1,7), (0,-55), (-123,1)]))

def quicksort(array):

    length = len(array)
    if length < 2:
        return array
    else:
        pivot = array[0]

        lower = [x for x in array[1:] if x < pivot]

        for x in array[1:]:
            if x < pivot:
                lower.append(x)

        higher = [x for x in array[1:] if x >= pivot]

        return quicksort(lower) + [pivot] + quicksort(higher)


print(quicksort([1,33,25,123,234235,12,2,0,1,3,4,5]))
