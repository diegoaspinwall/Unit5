#Diego Aspinwall
#10-15-17
#stat.py

print('Enter a list of numbers')
print('Enter "q" when done')

list = []

while True:
    q = input('>')
    if q == 'q':
        break
    else:
        list.append(q)
print(list)
