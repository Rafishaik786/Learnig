myl = eval(input('enter a list='))


def primes_in_list():
    c = []
    d = []
    for i in myl:
        num = i
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                c.append(num)
    for i in c:
        if i not in d:
            d.append(i)
    print(d)


primes_in_list()


