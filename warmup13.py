#Diego Aspinwall
#10-16-17
#warmup13.py

from random import randint

list = []

for i in range(0,20):
    list.append(randint(1,100))

print('Min:',min(list))
print('Max:',max(list))
print('Sum:',sum(list))
