mylist = [2, 3, 6, 5, 4, 8, 9, 7, 6, 4, 7, 8, 9, 3, 2, 14, 5, 6]


def eliminate_primes():
    uniquelist = []
    for i in mylist():
        if i not in primelist:
            uniquelist.append(i)


    for ele in primelist:
            if ele > 1:
                for i in range(2, ele):
                    if (ele % i) == 0:
                        break
                else:
                    primelist.append(ele)
    print(primelist)


eliminate_primes()