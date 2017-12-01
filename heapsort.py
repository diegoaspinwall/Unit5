#Diego Aspinwall
#10-27-17
#heapsort.py - implementation of heap sort w/ introsort

from random import randint
from time import time
from math import log

N = 100 #how many numbers will be sorted

#introsort
def sort(A):
    maxdepth = int(log(len(A)))*2
    introsort(A, maxdepth)

def introsort(A,maxdepth):
    n = len(A)
    if n<= 1:
        return
    elif maxdepth == 0:
        heapsort(A,N)
    else:
        p = partition(A, min(A), max(A))
        introsort(A[0:p], maxdepth-1)
        introsort(A[p+1:n], maxdepth-1)
'''
algorithm partition(A, lo, hi) is
    pivot := A[hi]
    i := lo - 1    
    for j := lo to hi - 1 do
        if A[j] < pivot then
            i := i + 1
            swap A[i] with A[j]
    if A[hi] < A[i + 1] then
        swap A[i + 1] with A[hi]
    return i + 1
'''
def partition(A, lo, hi):
    pivot = A[hi]
    i = lo-1
    for j in range(lo, hi-1):
        if A[j] < pivot:
            i=i+1
            A[i], A[j] = A[j], A[i]
    if A[hi] < A[i+1]:
        A[i+1], A[hi] = A[hi], A[i+1]
    return i+1

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
    #numbers = sort(numbers)
    numbers = heapsort(numbers, N)
    t2 = time()
       
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')

