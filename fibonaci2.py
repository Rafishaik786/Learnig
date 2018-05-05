def fibonaci(num):
    #num=int(input('enter a positive integer number:'))
    first=0
    second=1
    # count=0
    # while count < num:
    for i in range(num):
        print(first)
        temp=first
        first=second
        second+=temp
        # count+=1

fibonaci(10)