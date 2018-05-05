basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
fruits_count=0
non_fruit_count=0
for k,l in basket_items.items():
    if k in fruits:
        fruits_count += l
    else:
        non_fruit_count += l
print(fruits_count)
print(non_fruit_count)
for k,l in basket_items.items():
    print(k,':',l)