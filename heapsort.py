#Diego Aspinwall
#10-27-17
#heapsort.py - implementation of heap sort

from random import randint
from time import time
from math import log

N = 100 #how many numbers will be sorted

#heapsort
def iParent(i):
    return int((i-1)/2)
def iLeftChild(i):
    return (2*i + 1)
def iRightChild(i):
    return (2*i + 2)

def heapsort(a, count):
    heapify(a,count)
    end = count-1
    while end>0:
        a[end], a[0] = a[0], a[end]
        end = end-1
        siftDown(a,0,end)
    return a

def heapify(a,count):
    start = iParent(count-1)
    while start >= 0:
        siftDown(a,start,count-1)
        start = start-1

def siftDown(a, start, end):
    root = start
    while iLeftChild(root) <= end:
        child = iLeftChild(root)
        swap = root
        if a[swap] < a[child]:
            swap = child
        if child+1 <= end and a[swap] < a[child+1]:
            swap = child+1
        if swap == root:
            return
        else:
            a[root], a[swap] = a[swap], a[root]
            root = swap

if __name__ == '__main__':
    
    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
        
    pythonSort = sorted(numbers)#Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = heapsort(numbers, N)
    t2 = time()
       
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')

