def bubble(list_a):
    idxLength = len(list_a) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        
        for i in range(0, idxLength):
            if list_a[i] > list_a[i+1]:
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
                sorted = False
                
    return list_a

print(bubble([1,3,2,4,1,2]))