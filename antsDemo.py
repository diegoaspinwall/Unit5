#Diego Aspinwall
#11-20-17
#antsDemo.py - how to use lists with graphics

from ggame import *
from random import randint

WIDTH = 800
HEIGHT = 400
RAD = 5

def step():
    for ant in data['antList']:
        dx = randint(-4,3)
        dy = randint(-4,3)
        if ant.x+dx>0 and ant.x+dx<WIDTH:
            ant.x += dx
        if ant.y+dy>0 and ant.y+dy<HEIGHT:
            ant.y += dy

if __name__ == '__main__':
    
    data = {}
    data['antList'] = []
    
    red = Color(0x660000,1)
    ant = CircleAsset(RAD,LineStyle(1,red),red)
    
    for i in range(0,100):
        data['antList'].append(Sprite(ant,(randint(RAD,WIDTH),randint(RAD,HEIGHT))))
    
    App().run(step)
