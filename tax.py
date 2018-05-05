biryani=int(input('enter biryani price='))
full_meals=int(input('enter price of full meals='))
def tax(bill):
    #bill=int(input('enter your current bill to caluculate tax='))
    """adds 0.8% of tax to the current bill"""
    bill *=1.08
    #("the bill with the tax %r" %bill)
    return bill

def tip(bill):
   # bill = int(input('enter your current bill to caluculate  tip='))
    """ adds the 15 percentage of tip to the current bill"""
    bill *= 1.15
    # print("the bill with the tip of %r" %bill)
    return bill


biryani_with_tax=tax(biryani)
print('biryani_with_tax=',biryani_with_tax)
c=tax(full_meals)
print('cost of full meals with tax=',c)
biryani_with_tip=tip(biryani)
full_meal_with_tip=tip(full_meals)
print('biryani_with_tip=',biryani_with_tip)
print("full_meal_with_tip=",full_meal_with_tip)
#
