class Account:
    life=6
    def attack(self):
        print('dinga')
    def check(self):
        if self.life<6:
            print('iam fine')
        else:
            print('its not fine')

act=Account()
act.attack()
act.check()
