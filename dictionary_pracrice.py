cast = {
           "Jerry Seinfeld": "Jerry sopefeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
#cast['name':'rafi']
#print(cast)
#def count():
    #for i,y in cast.items():
        #print("{} is the wife of{}".format(i,y))


basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
result=0
for fruit, k in basket_items.items():
    if fruit in fruits:
        result +=k
print(result)