jk=[1,2,3,4,5,6,9,8,7,4]

def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(jk)
