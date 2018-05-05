def is_prime(num):
    v=[1,2,3,4,5,6,7,8,9]
    if num>1:
        for i in range(2, num):
            if num%i==0:
                print(num,'is not prime')
                break
        print(num,'is a prime number')
    else:
        print(num,'is not a prime number')


is_prime(2)
v = [1, 2, 3, 4, 5, 6, 7, 8, 9]
map(is_prime,v)