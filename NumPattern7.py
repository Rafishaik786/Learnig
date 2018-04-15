def pattern7():
    num=int(input('enter a number='))
    for i in range(num,0,-1):
        for j in range(1,i+1):
            print(i,end=' ')
        print()
pattern7()