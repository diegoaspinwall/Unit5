#Diego Aspinwall
#12-4-17
#quiz5.py - testing our knowledge

from random import randint

def rand5():
    nums = []
    for i in range(0,5):
        nums.append(randint(1,100))
    return nums

def lastElement(list):
    return list[-1]

def wordLengths():
    

print(rand5())
print(lastElement(['cat','dog','rat']))
