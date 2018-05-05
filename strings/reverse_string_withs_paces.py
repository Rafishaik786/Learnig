input_string = input('enter a string=')


def dinga():
    empty = ' '
    for i in input_string:
        if i == ' ':
            empty += ' '
        else:
            empty = i+empty
    print(empty)

def reverse():
    name='my name is rafi'
    num=list(name)
    urgent=[]
    for i in num:
        if i==' ':
            urgent.append(' ')
    print(urgent)


reverse()

