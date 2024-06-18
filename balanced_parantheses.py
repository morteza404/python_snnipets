o = "{"
c = "}"

def draw(n):
    lst = []
    if n == 0:
        return
    for _ in range(n):
        lst.append(o)
    for i in lst:
        print(i, c, sep="", end="")

draw(2)