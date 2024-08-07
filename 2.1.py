msg='Welcome to Python 101: Strings'
print(msg.replace('Python','C'))
msg1=msg.replace('Python','Java')
print(msg1)

# membership

print('java' in msg)
print('c' in msg)
print('C' not in msg1)

name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color.lower() + '!'
msg1 = f'[{name}] loves the color {color.lower()}!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg)
print(msg1)

