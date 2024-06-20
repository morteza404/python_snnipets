def match(s1):
    for _ in range(len(s1)):
        s1 += ")"
    return s1


def combinations(n):
    s = ""
    for i in range(n):
        s += "("
    k = len(s)
    for i in range(1, k + 1):
        print(match(s[:i]), match(s[i:]))


if __name__ == "__main__":    
    combinations(4)
