k=[1,5,9,7,3,4,11,22,8]
l=[1,4,5,8,7,9,6,5,4,2]
li=[x*3 for x in l]
print(li)
f=set(filter(lambda k :(k%2==0),l))
print(f)
g=map(lambda v: (v*2),l)
print(g)
h=(lambda x,y:(x+y),l)
# >>> foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# >>>
print(filter(lambda x: x % 3 == 0, l))
# [18, 9, 24, 12, 27]
# >>>
# >>> print map(lambda x: x * 2 + 10, foo)
# [14, 46, 28, 54, 44, 58, 26, 34, 64]
# >>>
# >>> print reduce(lambda x, y: x + y, foo)
# 139