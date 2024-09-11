lst = [10, 6, 4, 8, 9, 1, 3, 2, 5, 7]

def bubble_sort(lst):
    newLst = lst
    for i in range(len(newLst)-1):
        print("i: " + str(i))
        for j in range(len(newLst)-1):
            print("j: " + str(j))
            if newLst[j] > newLst[j+1]:
                aux = newLst[j]
                newLst[j] = newLst[j+1]
                newLst[j+1] = aux

            print(newLst)
    
    print("FINAL:")
    print(newLst)

bubble_sort(lst)