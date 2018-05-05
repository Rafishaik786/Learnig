fruits=[('apple',14),('mango',16),('banana',34),('pine_apple',46),('papaya',33)]
truck=[]
weight=0
for i, j in fruits:
    if weight >= 100:
       # print('sorry weight out of bounds')
        break
    else:
        truck.append(i)
        weight+=j
print(truck)
print('truck load weight=',weight)
