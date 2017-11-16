#Diego Aspinwall
#10-16-17
#warmup13.py

from random import randint

num = []

for i in range(0,20):
    num.append(randint(1,100))

print('Min:',min(num))
print('Max:',max(num))
print('Sum:',sum(num))
