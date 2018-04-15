class First(object):
    v=12
    def sample(self):
        print('this is sample method')
    def test(self):
        print('this is test method')
class Second(First):
    def enimy(self):
        print('this is enimy method')
    def soilder(self):
        print('this is soilder method')

sum=Second()

sum.enimy()
sum.soilder()
print(sum.v)
print(First.v)
sum.sample()
sum.test()