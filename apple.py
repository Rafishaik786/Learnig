class Apple:
    b = 10

    def __init__(self, name, age, sal, v):
        self.name = name
        self.age = age
        self.sal = sal
        self.v = v

    def cooking(self):
        print('this is ding')

    def singing(self):
        print('sing song')


sun = Apple('ani', 23, 10000, 1)
dani =Apple("john", 22, 25000,2)
print('name=', dani.name,  'age=', dani.age,  'sal=', dani.sal, 'v=', dani.v)
print('name=', sun.name,  'age=', sun.age,  'sal=', sun.sal, 'v=', sun.v)
print('b =', sun.b)
sun.cock()
dani.cock()
sun.singing()
sun.b = 20
dani.b = 50
print('b =', sun.b)
print('b =', dani.b)
print(Apple.b)
