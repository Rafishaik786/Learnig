line = input('enter a string=')
key1=input('enter first key=')
key2=input('enter second key=')
value1=input('enter the first value=')
value2=input('enter the second value=')
#s='shaik'
f=''
for char in line:
    if char==key1:
        f+=value1
    elif char == key2:
        f+=value2
    else:
        f+=char
print(f)