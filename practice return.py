d=[1,2,3,4,5,6,7,8,9,10,11,12,13]
def red(*args):
    g=[]
    for i in d:
        if i%2!=0:
            g.append(i)
    return g


print(red(*d))