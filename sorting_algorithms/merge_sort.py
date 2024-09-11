'''

1. Divide the list in two halves.
2. Send each list to get sorted.
3. If the list received is length 1 or less, return it.
4. Join list comparing the first element of each list. 

'''

lst = [10, 6, 4, 8, 9, 1, 3, 2, 5, 7]

def merge_sort(lst):
    if len(lst) <= 1: return lst

    midIndex = (len(lst) // 2)

    half1 = merge_sort(lst[:midIndex])
    half2 = merge_sort(lst[midIndex:])

    print(half1)
    print(half2)
    print("\n")

    newLst = []
    i = 0
    j = 0
    while i < len(half1) and j < len(half2):
        if half1[i] < half2[j]:
            newLst.append(half1[i])
            i += 1
        else:
            newLst.append(half2[j])
            j += 1
    
    while i < len(half1):
        newLst.append(half1[i])
        i += 1

    while j < len(half2):
        newLst.append(half2[j])
        j += 1

    return newLst

newLst = merge_sort(lst)

print(newLst)