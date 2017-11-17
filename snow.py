#Diego Aspinwall
#11-17-17
#snow.py

from ggame import *

def spriteflake():
    fallflake.x = SIZE*randint(0,COLS)
    data['frames'] = 0

def step():
    data['frames'] += 1
    if data['frames'] == 200:
        spriteflake()

if __name__ == '__main__':
    
    COLS = 20
    SIZE = 15
    
    white = Color(0xffffff,1)
    backg = Color(0x000000,1)
    backgOutline = LineStyle(1,backg)
    whiteOutline = LineStyle(1,white)
    
    backgRectangle = RectangleAsset(COLS*SIZE,COLS*SIZE,backgOutline,backg)
    snowBlock = RectangleAsset(SIZE,SIZE,whiteOutline,white)
    
    fallflake = Sprite(paddleBox)
    
    Sprite(backgRectangle)
    App().run(step)
