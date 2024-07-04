from itertools import islice

"""
python 3.12:
            from itertools import batched
"""


def batched(iterable, n):
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched("ABCDEFG", 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


for i in batched("ABCDEFG", 3):
    print(i)
