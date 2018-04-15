def palindrome():
    lower=int(input("enter starting  number:"))
    higher = int(input("enter ending  number:"))
    for num in range(lower,higher):
        temp=num
        rev=0
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num=num//10
        if(temp==rev):
            print( temp,)
        else:
            pass

palindrome()




