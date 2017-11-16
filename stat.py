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

median = str(list[len(list)/2])
if len(list)%2 == 0:
    median = median, 'and', str(list[(len(list)/2)-1])

list.sort()
print(list)
print('Min:',min(list))
print('Mean:',sum(list)/len(list))
print('Median:',median)
print('Max:',max(list))
