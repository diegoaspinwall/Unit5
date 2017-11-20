#Diego Aspinwall
#11-17-17
#snow.py

from ggame import *
from random import randint

def spriteflake():
    data['flakes'].append(Sprite(snowBlock, (SIZE*randint(0,COLS-1),0)))
    data['frames'] = 0
    

def step():
    data['frames'] += 1
    if data['frames'] == 10:
        spriteflake()
    for flake in data['flakes']:
        flake.y += 5


if __name__ == '__main__':
    
    data = {}
    data['frames'] = 0
    data['flakes'] = []
    
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

'''
  for ant in data['antList']:
        dx = randint(-4,3)
        dy = randint(-4,3)
        if ant.x+dx>0 and ant.x+dx<WIDTH:
            ant.x += dx
        if ant.y+dy>0 and ant.y+dy<HEIGHT:
            ant.y += dy
'''
