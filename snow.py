#Diego Aspinwall
#11-17-17
#snow.py

from ggame import *
from random import randint

def spriteflake():
    fallflake = Sprite(snowBlock, (SIZE*randint(0,COLS-1),0))

def step():
    data['frames'] += 1
    if data['frames'] == 20:
        spriteflake()
        data['frames'] = 0
    fallflake.y += 1


if __name__ == '__main__':
    
    data = {}
    data['frames'] = 0
    
    COLS = 30
    SIZE = 10
    
    white = Color(0xffffff,1)
    backg = Color(0x000000,1)
    backgOutline = LineStyle(1,backg)
    whiteOutline = LineStyle(1,white)
    
    backgRectangle = RectangleAsset(COLS*SIZE,COLS*SIZE,backgOutline,backg)
    snowBlock = RectangleAsset(SIZE,SIZE,whiteOutline,white)
    
    Sprite(backgRectangle)
    App().run(step)
