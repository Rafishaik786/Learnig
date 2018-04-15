def isArmstrong():
    num=int(input('enter a number='))
    temp = num
    order = len(str(num))
    sum = 0
    while temp > 0:
        digit = temp % 10  # swaping last digit
        sum += digit ** order
        temp //= 10  # chefking whether all digits are completed or not
    if num == sum:
            print(num,'is arm strong number')
    else:
            print(num,'is not arm strong number')

isArmstrong()
