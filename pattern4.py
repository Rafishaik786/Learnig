def pattern4():
    num=int(input('enter a number='))
    for r in range(1,num+1):
        for c in range(1,r+1):
            print(c,end=' ')

        print()

pattern4()