class Methods:
    def __init__(self,name):
        self.name=name

    def sample(self,name):
        print('hello', self.name)
    @classmethod
    def classMethod(cls,):
        print('this is class method')
    @staticmethod
    def staticMethod():
         print('this is static method')
for i in range(10):
    print('hello')
    xx=Methods('ram')
yy=Methods('ravi')
print("name=",xx.name)
print("name=",yy.name)
xx.sample('ranga')

Methods.classMethod()
yy.classMethod()
Methods.staticMethod()
yy.staticMethod()