x=int(input('enter a number:'))
y=int(input('enter a number:'))
try:
    z=x/y
except Exception as e:
    print('exception occured as e:', e)
    raise
#except TypeError:
    #print('value cannotbe divided with zero')