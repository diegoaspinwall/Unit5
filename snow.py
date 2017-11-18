#Diego Aspinwall
#11-17-17
#snow.py

from ggame import *

def spriteflake():
    Sprite(snowBlock, (30,30))

def step():
    data['frames'] += 1
    if data['frames'] == 20:
        spriteflake()
        data['frames'] = 0

if __name__ == '__main__':
    
    data = {}
    data['frames'] = 0
    
    COLS = 20
    SIZE = 15
    
    white = Color(0xfff00f,1)
    backg = Color(0x000000,1)
    backgOutline = LineStyle(1,backg)
    whiteOutline = LineStyle(1,white)
    
    backgRectangle = RectangleAsset(COLS*SIZE,COLS*SIZE,backgOutline,backg)
    snowBlock = RectangleAsset(SIZE,SIZE,whiteOutline,white)
    
    #Sprite(backgRectangle)
    App().run(step)
