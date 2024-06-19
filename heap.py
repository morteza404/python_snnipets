import heapq


def heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]

lst = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

print(heap_sort(lst))