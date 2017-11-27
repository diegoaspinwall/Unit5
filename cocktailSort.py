#Diego Aspinwall
#10-27-17
#cocktailSort.py - implementation of cocktail sort

from random import randint
from time import time

N = 100 #how many numbers will be sorted

'''
procedure cocktailShakerSort( A : list of sortable items ) defined as:
  do
    swapped := false
    for each i in 0 to length( A ) - 2 do:
      if A[ i ] > A[ i + 1 ] then // test whether the two elements are in the wrong order
        swap( A[ i ], A[ i + 1 ] ) // let the two elements change places
        swapped := true
      end if
    end for
    if not swapped then
      // we can exit the outer loop here if no swaps occurred.
      break do-while loop
    end if
    swapped := false
    for each i in length( A ) - 2 to 0 do:
      if A[ i ] > A[ i + 1 ] then
        swap( A[ i ], A[ i + 1 ] )
        swapped := true
      end if
    end for
  while swapped // if no elements have been swapped, then the list is sorted
end procedure
'''

def mySort(A):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0,len(A)-1):
            if A[i]>A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]#how you swap
                swapped = True
        
    return A

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
