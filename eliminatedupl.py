mylist = eval(input('enter a list='))


def eliminate_repeated():
    super1 = []
    even_list = []
    odd_list = []
    for i in mylist:
        if i not in super1:
            super1.append(i)
    print("my first yield ")
    yield super1

    for i in mylist:
        if i % 2 == 0:
            even_list.append(i)
    print("my second yield")
    yield even_list

    for i in mylist:
        if i % 2 !=0:
            odd_list.append(i)
    yield odd_list
    print("my third yield")


gen=eliminate_repeated()
print(next(gen))
print(next(gen))
print(gen)