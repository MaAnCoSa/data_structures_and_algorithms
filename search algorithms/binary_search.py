lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(lst, item):
    newLst = lst
    fix = 0
    while True:
        i = len(newLst) // 2

        print(newLst, fix+i, newLst[i])

        if newLst[i] == item:
            return (i, newLst[i])
        elif newLst[i] < item:
            fix += i
            newLst = newLst[i:]
        elif newLst[i] > item:
            newLst = newLst[:i]
    
binary_search(lst, 10)