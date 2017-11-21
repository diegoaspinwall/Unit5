#Diego Aspinwall
#11-17-17
#snow.py

from ggame import *
from random import randint

def spriteflake():
    xpos = randint(0,COLS-1)
    data['flakes'].append(Sprite(snowBlock, (SIZE*xpos,0)))
    data['frames'] = 0
    data['fallpos'][xpos] += 1
    

def step():
    data['frames'] += 1
    if data['frames'] == 10:
        spriteflake()
    for flake in data['flakes']:
        flake.y += 1
        if flake.y == (COLS*SIZE):
            data['flakes'].remove(flake)


if __name__ == '__main__':
    
    data = {}
    data['frames'] = 0
    data['flakes'] = []
    data['fallpos'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    COLS = 100
    SIZE = 3
    
    white = Color(0xffffff,1)
    backg = Color(0x000000,1)
    backgOutline = LineStyle(1,backg)
    whiteOutline = LineStyle(1,white)
    
    backgRectangle = RectangleAsset(COLS*SIZE,COLS*SIZE,backgOutline,backg)
    snowBlock = RectangleAsset(SIZE,SIZE,whiteOutline,white)
    
    Sprite(backgRectangle)
    App().run(step)
