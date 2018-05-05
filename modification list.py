names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
username=[]
for name in names:
    username.append(name.lower().replace(' ','_'))
print(username)
print('/n')
values=['Thoman Khan','Jorge David','Jodha Akbar']
for i in range(len(values)):
    values[i] = values[i].lower().replace(' ','_')
print(values)