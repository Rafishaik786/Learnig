def strong_number():
    num = int(input('enter a number:'))
    temp = num
    jum= 0
    while num:
        i = 1
        f = 1
        r = num%10
        while i <= r:
            f = f*i
            i = i+1
        jum = jum+f
        num=num//10
    if(jum == temp):
        print(  temp ,'is a strong number')
    else:
        print( temp, "is not a strong number")


strong_number()

