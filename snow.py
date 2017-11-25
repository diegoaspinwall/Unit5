#Diego Aspinwall
#11-17-17
#snow.py

from ggame import *
from random import randint

def spriteflake():
    xpos = randint(0,COLS-1)
    data['flakes'].append(Sprite(snowBlock, (SIZE*xpos,-SIZE)))
    data['fallpos'][xpos] += 1
    data['stopflake'].append(data['fallpos'][xpos])
    print(data['stopflake'])
    

def step():
    data['frames'] += 1
    if data['frames'] == 10:
        spriteflake()
        data['frames'] = 0
    place = 0
    for flake in data['flakes']:
        flake.y += 1
        if flake.y == ((COLS-1)*SIZE-SIZE*(data['stopflake'][place])):
            data['flakes'].remove(flake)
            data['stopflake'].remove(data['stopflake'][place])
        place += 1


if __name__ == '__main__':
    
    COLS = 100
    SIZE = 3
    
    data = {}
    data['frames'] = 0
    data['flakes'] = []
    data['fallpos'] = []
    data['stopflake'] = []
    for i in range(0,COLS):
        data['fallpos'].append(0)

    white = Color(0x00ffff,1)
    backg = Color(0x000000,1)
    backgOutline = LineStyle(1,backg)
    whiteOutline = LineStyle(1,white)
    
    backgRectangle = RectangleAsset(COLS*SIZE,COLS*SIZE,backgOutline,backg)
    snowBlock = RectangleAsset(SIZE,SIZE,whiteOutline,white)
    
    Sprite(backgRectangle)
    App().run(step)
