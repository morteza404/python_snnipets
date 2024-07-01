lst = [0, 1]


def fibo(n):
    if n < len(lst):
        return lst[n]
    lst.append(fibo(n - 1) + fibo(n - 2))
    return lst[n]


print(fibo(10))
