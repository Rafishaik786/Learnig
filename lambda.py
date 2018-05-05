p = lambda  x: x%2==0
print(p(5))
m = [1,2,3,6,5,4,7,8,9,5,4,1,2,5,6,45,4]
n=[]
for i in m:
    if i not in n:
        n.append(i)
print(n)
p=list(filter(lambda f:f%2==0,n ))

print(p)

