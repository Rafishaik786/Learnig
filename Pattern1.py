def pattern():
    num=int(input('enter a number='))
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(' *',end='')
        print()
pattern()
class poligon(object):
        name='john'



poli=poligon()
setattr(poli,'name','rafi')
print(poli.name)