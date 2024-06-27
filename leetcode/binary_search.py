def search(a, target):
    if len(a) == 0:
        return False
    mid = len(a) // 2
    if a[mid] == target:
        return True
    elif a[mid] > target:
        return search(a[:mid], target)
    else:
        return search(a[mid + 1 :], target)
    
lst = [10,20,30,45,55,65,70,89,93]
target = 22
print(search(lst, target))
