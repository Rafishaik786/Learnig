k = [1, 2, 5, 8, 6, 7, 3, 4, 7]
l = [10, 11, 12, 4, 15, 17, 18]


def ground(*name):
    f=sum(name)
    print(f)

ground(*k,*l)
i = {'b': 'nani','mum': 83320}


def play(**joc):
    print(joc)

play(**i)
