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

list.sort()

median = (list[len(list)/2])
if len(list)%2 == 0:
    median = median, 'and', (list[(len(list)/2)-1])

high = list.count(list[0])
num = list[0]
for i in list:
    if list.count(i)>high:
        high = list.count(i)
        num = list[i-1]

print(list)
print('Min:',min(list))
print('Mean:',sum(list)/len(list))
print('Median:',median)
print('Mode:',num)
print('Max:',max(list))
