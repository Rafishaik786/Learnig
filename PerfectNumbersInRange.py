def perfectInRange():
    lower = int(input('enter lower number:'))
    higher = int(input('enter higher number:'))
    for i in range(lower, higher):
        sum = 0
        temp = i
        for j in range(1, temp):
            if (temp % j == 0):
                sum = sum + j
        if (sum == temp):
            print(temp,)


perfectInRange()