input_string = input('enter a string=')


def dinga():
    empty = ' '
    for i in input_string:
        if i == ' ':
            empty += ' '
        else:
            empty = i+empty
    print(empty)

