#Diego Aspinwall
#10-16-17
#warmup13.py

from random import randint

nums = []

for i in range(0,20):
    num = randint(1,100)
    nums.append(num)


print('Min:',min(int(nums)))
print('Max:',max(int(nums)))
print('Sum:',sum(int(nums)))
