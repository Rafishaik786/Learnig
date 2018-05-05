l=[1,5,6,9,8]
print(len(l))
l.append(55)
print(l)
k=l.append(52)#append method does not hold any value it just append it
print(l)
print(k)

l.append(666)
print(l)

l.append(777)
print(l)
print(len(l))
k=len(l)
print(k)
del l[4]
print(l)