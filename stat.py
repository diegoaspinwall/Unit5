#Diego Aspinwall
#10-15-17
#stat.py

print('Enter a list of numbers')
print('Enter "q" when done')

list = []

while True:
    qsearch = input('>')
    if qsearch == 'q':
        break
    else:
        list.append(int(qsearch))
print(list)
list.sort()
print(list)
print('Min:',min(list))
print('Mean:',sum(list)/len(list))
print('Median:')
print('Max:',max(list))
