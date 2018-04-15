from random import randint
def sumOfRandom():
    sum = 0
    for i in range(1,6):
        a = randint(10, 99)
        print(a,'+',sum,'=',a+sum)

        sum = sum + a
    print('total sum ={}'.format(sum))

sumOfRandom()