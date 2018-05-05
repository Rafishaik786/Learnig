class Methods:
    def __init__(self,name):
        self.name = name

    def sample(self,name):
        print('hello', self.name)

    @classmethod
    def vertical(cls):
        print('this is class method')

    @staticmethod
    def double():
        print('this is static method')


xx = Methods('ram')
yy = Methods('ravi')
print("name=",xx.name)
print("name=",yy.name)
xx.sample('ranga')

Methods.vertical()
yy.vertical()
Methods.double()
yy.double()