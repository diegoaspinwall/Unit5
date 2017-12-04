#Diego Aspinwall
#12-4-17
#quiz5.py - testing our knowledge

from random import randint

def rand5():
    nums = []
    for i in range(0,5):
        nums.append(randint(1,100))
    return nums

def lastElement(aist):
    return aist[-1]

def wordLengths(bist):
    outlist = []
    for word in bist:
        outlist.append(len(word))
    return outlist

def biggest(cist):
    


print(rand5())
print(lastElement(['cat','dog','rat']))
print(wordLengths(['the','cat','is','hungry']))
print(biggest([3,-1,5,-2,7,2,1]))
