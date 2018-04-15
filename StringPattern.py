def strPattern():
    name=input('enter a name=')
    length=len(name)
    for row in range(length):
        for col in range(row+1):
            print(name[col],end='')
        print()
strPattern()
