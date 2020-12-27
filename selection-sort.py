

def selectionSort(list_a):
    idxLength = range(0, len(list_a) -1)
    
    for i in idxLength:
        minVal = i
    
        for j in range(i + 1, len(list_a)):
            if (list_a[j] < list_a[minVal]):
                minVal = j
                
            if minVal != i:
               list_a[minVal], list_a[i] =  list_a[i], list_a[minVal]
                
    return list_a

print(selectionSort([2,3,7,8,3,4,2]))