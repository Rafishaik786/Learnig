def practice():
    f = []
    n=1
    for i in range(1,15):
        f.append(n)
        n = n+1
    print(f)
    print(len(f))

    print(f.pop(5))

    print(f.sort())
    print(f)
    f.insert(5,5)
    print(f)
    f.remove(14)
    print(f)

    f.pop()
    print(f)
    f.pop(5)
    print(f)
    f.count('o')
    print(f)
