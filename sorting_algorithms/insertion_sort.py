lst = [10, 6, 4, 8, 9, 1, 3, 2, 5, 7]

def insertion_sort(lst):
    newLst = lst
    for j in range(len(newLst)):
        if j == 0: continue
        i = j
        aux = newLst.pop(i)
        while i-1 >= 0 and aux < newLst[i-1]:
            i -= 1
        newLst.insert(i, aux)

        print(newLst)

insertion_sort(lst)
