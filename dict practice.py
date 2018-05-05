# s={'fruit':'banana','phal':'banana','frui':'mango'}
# print(s)
# s[1:2]
#d=[x**2 for x in range(1,10) ]
l=[1,2,5,7,6,9,7,5]
l.pop()
print(l)
print(l.pop(2))


l.remove(1)
print(l)
print(l.remove(2))

l.insert(11,15)
print(l)

l.pop()
del l [l.index(7)]
print(l)

d={'a':'ba','c':'ca'}
print(d)
a=[1,2,3,4,5,6,7,8,9,4]
k=[5,8,9,7,4,5,6,12,3]
d=dict(zip(a,k))
print(d)
print(d[1])
#print(type(zip()))

