import random
count = 0
while count<3:
    t = random.randint(1,6)
    print(t)
    if t == 5:
        print('u loss ')
        break
        count += 1
    else:
        print(' u win')