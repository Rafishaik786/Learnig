def pattern8():
    num=int(input('enter a number='))
    n=1
    for i in range(num,0,-1):
        for j in range(1,i+1):
            print( n,end=' ')
            n=n+1
        print()

pattern8()