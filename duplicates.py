# a=int(input('enter a number'))
# b=int(input('enter second number'))
# a,b=b,a
# print(a)
# print(b,end='')
k=eval(input('enter a list of numbers'))
def ele():
    d=[]
    for i in k:
        if i not in d:
            d.append(i)
    return d

print(ele())


