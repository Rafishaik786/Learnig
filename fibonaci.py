def fibonaci(n):
    if(n<=1):
        return n
    else:
        return(fibonaci(n-1)+fibonaci(n-2))
n=int(input("enter a number:"))
print('fibonaci sequence:')
for i in range(n):
        print( fibonaci(i))