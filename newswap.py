def swap():
    a = eval(input('enter a number='))
    b = eval(input('enter a number='))
    print(a,b)
    if a>b:

        a-=a-b
        b+=a-b
        print(a,b)
    elif b>a:
        a+=b-a
        b-=b-a
        print(a,b)
    elif a==b:
        print(a,b)
    else :
        print('invalid numbers')

swap()
a=eval(input("Enter value of first variable: "))
b=eval(input("Enter value of second variable: "))
a=a+b
b=a-b
a=a-b
print("a is:",a," b is:",b)

