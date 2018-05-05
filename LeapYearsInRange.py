def leapYear():
    lower = int(input("Enter lowest year: "))
    higher = int(input("Enter highest year: "))
    for year in range(lower,higher):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                   print(year,)
                else:
                    print(year, )
            else:
                print(year,)


leapYear()