lst = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]

def linear_search(lst, item):
    for i in lst:
        if i == item: 
            print(i)
            return i
    print("not found")
    return "not found"

linear_search(lst, 10)