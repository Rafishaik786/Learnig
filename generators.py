def factorial(n):
    fact=[]
    k=1
    for i in range(1,n+1):
        k*=i
        fact.append(k)
        print(fact)
        return fact

factorial(10)


