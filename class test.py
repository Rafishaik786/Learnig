class Account(object):
    life=6
    def attack(self):
        c=555
        if c<55:
            print('dinga')
        else:
            print('manga')
    def check(self):
        if self.life<6:
            print('iam fine')
        else:
            print('its not fine')
    @classmethod
    def anywhere(cls,name):
        print(name,'mama')
    @staticmethod
    def somewhere():
        print('flowers')

act=Account()
act.attack()
act.check()
act.anywhere('funny')
Account.anywhere('rafi')
act.somewhere()
Account.somewhere()

