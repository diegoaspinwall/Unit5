#Diego Aspinwall
#11-27-17
#connectFour.py

from ggame import *

def printBoard():
    for row in range(0,6):
        for col in range(0,7):
            Sprite(hole, (110*col+60, 110*row+60))

if __name__ == '__main__':
    
    white = Color(0xffffff,1)
    red = Color(0xff0000,1)
    blue = Color(0x0000ff,1)
    black = Color(0x000000,1)
    blackOutline = LineStyle(1,black)
    
    hole = CircleAsset(50,blackOutline,white)
    
    printBoard()
    
    App().run()