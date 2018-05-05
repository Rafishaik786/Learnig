import random


def sum_of_random():
    sum = 0
    for i in range(1,6):
        a = random.randint(10, 99)
        print(a,'+',sum,'=',a+sum)

        sum = sum + a
    print('total sum ={}'.format(sum))

sum_of_random()