def numPattern6():
    num=int(input('enter a number='))
    for i in range(num,0,-1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()
numPattern6()

