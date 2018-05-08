d=[1,5,4,7,8,9,3,4,25,15,14]
def num(*args):
    sum=0
    for i in range(0,len(args)):
        sum+=args[i]
    print(sum)

num(*d)