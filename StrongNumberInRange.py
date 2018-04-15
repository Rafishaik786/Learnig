def strongNumber():
    lower = int(input('enter lower number:'))
    higher = int(input('enter higher number:'))
    for i in range(lower,higher):
        temp=i
        sum = 0
        while(i):
            v=1
            f=1
            r=i%10
            while(v<=r):
                f=f*v
                v=v+1
            sum=sum+f
            i=i//10
        if(sum==temp):
            print(  temp ,)


strongNumber()

