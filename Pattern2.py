def pattern2():
    num=int(input('enter a number='))
    for i in range(num,0,-1):
        for j in range(0,i):
            print(' *',end='')
        print()
pattern2()