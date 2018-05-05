lower = int(input('enter the lowest year='))
higher =int(input('enter the highest year='))
for year in range(lower,higher+1):
    if year %4 == 0:
        print(year)
