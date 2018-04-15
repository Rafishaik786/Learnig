def armstrong():
    num = int(input('enter a number:'))
    temp = num
    order = len(str(num))
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum +=digit ** order
        temp //= 10
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
        print ("i am going to use git now")

armstrong()