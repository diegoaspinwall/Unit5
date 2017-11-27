#Diego Aspinwall
#10-27-17
#cocktailSort.py - implementation of cocktail sort

from random import randint
from time import time
from math import log

N = 1000 #how many numbers will be sorted

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
procedure sort(A : array):
    let maxdepth = ⌊log(length(A))⌋ × 2
    introsort(A, maxdepth)

procedure introsort(A, maxdepth):
    n ← length(A)
    if n ≤ 1:
        return  // base case
    else if maxdepth = 0:
        heapsort(A)
    else:
        p ← partition(A)  // assume this function does pivot selection, p is the final position of the pivot
        introsort(A[0:p], maxdepth - 1)
        introsort(A[p+1:n], maxdepth - 1)

def mySort(A):
    maxdepth = int(log(len(A)))*2
    sort(A, maxdepth)

def sort(A, maxdepth):
    n = len(A)
    if n<=1:
        return
    elif maxdepth == 0:
        heapsort(A)
    else:
        p = partition(A)
        introsort(A[0:p+1], maxdepth-1)
        introsort(A[p+1:n+1], maxdepth-1)
'''

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
