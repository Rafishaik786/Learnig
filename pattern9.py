def triangle():
    num=int(input('enter a number='))
    for i in range(num):
        print(''*(num-i-1)+'*'*(2*i+1))
triangle()