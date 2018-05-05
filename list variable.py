def validation():
    num = int(input('enter a number='))
    if num == 7:
        print('this is the number')
        return
    return validation()


validation()
