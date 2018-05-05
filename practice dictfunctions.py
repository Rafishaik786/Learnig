# g={}
# g['name']='shail'
# g['clg']='nimra'
# g['university']='jntuk'
# print(g)
# g['clg']='houra'
# print(g)
# s=g.get('clg')
# print(s)
# print(g.copy())
# p=g.items()
# print(p)
# n=g.values()
# print(n)
# ns=g.keys()
# print(ns)
# g.pop('clg')
# print(g)
# g.popitem()
# print(g)
# g.setdefault(22552)
# print(g)
# g[22552]='phool'
# print(g)
# li=[1,2,3,6,5,4,7,89,9]
# m={}
# m=m.fromkeys(li)
# print(m)
# m.update(g)
# print(m)
# g.update(m)
g={1:'rafi',2:'lalli',3:'pavani'}
h={4:'lalli',5:'pavani'}
g.update(h)
print(g)