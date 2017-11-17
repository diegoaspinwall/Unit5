#Diego Aspinwall
#11-17-17
#matrixDmo.py - how to create/use a matrix

def printBoard():
    for row in range(0,3):
        for col in range(0,3):
            print(board[row][col],' ',end = '')
        print()

board = [['a','b','c'],['d','e','f'],['g','h','i']]
printBoard()

row = int(input('Enter a row number: '))
col = int(input('Enter a column number: '))

borad[row][col] = 'X'
