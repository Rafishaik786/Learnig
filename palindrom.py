def palindrome():
    num=int(input("enter a number:"))
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num//=10
    if(temp==rev):
        print( temp, 'is a palindrome',)
    else:
        print(temp,'is not a palindrome',)

palindrome()




