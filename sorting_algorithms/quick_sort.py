'''

1. Select pivot (lets use the last element).
2. Send pivot to end.
3. Partition array into smaller than pivot and larger than pivot.
4. Send each partition to the same algorithm and get it ordered
5. Concatenate back smaller - pivot - larger.
6. If array has 1 or less elements, return array as is.

'''

lst = [10, 6, 4, 8, 9, 1, 3, 2, 5, 7]

def quick_sort(lst):
    if len(lst) <= 1: return lst

    pivot = lst[len(lst)-1]
    prevLst = []
    afterLst = []
    for i in range(len(lst)-1):
        if lst[i] <= pivot:
            prevLst.append(lst[i])
        elif lst[i] >= pivot:
            afterLst.append(lst[i])

    print(prevLst)
    print(pivot)
    print(afterLst)
    return quick_sort(prevLst) + [pivot] + quick_sort(afterLst)

newLst = quick_sort(lst)

print("\nORDERED LIST:")
print(newLst)