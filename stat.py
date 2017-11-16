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
print('Min:',min(list))
print('Mean:',(sum(list)/len(list)))
print('Max:',max(list))
