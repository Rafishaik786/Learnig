#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

def armStrungNumbers():
    lower = int(input("Enter lower range: "))
    upper = int(input("Enter upper range: "))
    for num in range(lower, upper + 1):
        temp = num
        order = len(str(num))
        sum = 0
        while temp > 0:
            digit = temp % 10#swaping last digit
            sum += digit ** order
            temp //= 10# chefking whether all digits are completed or not

        if num == sum:
            print(num)

armStrungNumbers()