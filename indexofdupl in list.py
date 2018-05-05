num = eval(input('enter a list of number='))
num1 = int(input('enter a number='))


def check():
    new = []

    for position, item in enumerate(num,1):
        if item == num1:
            new.append(position)
    print(new)
    for i in enumerate(num):
        print(i)


check()