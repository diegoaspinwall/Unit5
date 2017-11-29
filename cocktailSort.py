#Diego Aspinwall
#10-27-17
#cocktailSort.py - implementation of cocktail sort

from random import randint
from time import time
from math import log

N = 100 #how many numbers will be sorted

'''
def mySort(A):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0,len(A)-1):
            if A[i]>A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]#how you swap
                swapped = True
        if not swapped:
            break
        swapped = False
        for i in range(len(A)-2,-1,-1):
            if A[i]>A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                swapped = True
    return A
'''
'''
procedure siftDown(a, start, end) is
    root ← start

    while iLeftChild(root) ≤ end do    (While the root has at least one child)
        child ← iLeftChild(root)   (Left child of root)
        swap ← root                (Keeps track of child to swap with)

        if a[swap] < a[child]
            swap ← child
        (If there is a right child and that child is greater)
        if child+1 ≤ end and a[swap] < a[child+1]
            swap ← child + 1
        if swap = root
            (The root holds the largest element. Since we assume the heaps rooted at the
             children are valid, this means that we are done.)
            return
        else
            swap(a[root], a[swap])
            root ← swap            (repeat to continue sifting down the child now)
'''

#heapsort
iParent(i)     = int((i-1) / 2)
iLeftChild(i)  = 2*i + 1
iRightChild(i) = 2*i + 2

def heapsort(a, count):
	end = count-1
	while end>0:
	    a[end], a[0] = a[0], a[end]
	    end = end-1
	    siftDown(a,0,end)

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
            


if __name__ == '__main__':
    
    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
        
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    t2 = time()
       
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
