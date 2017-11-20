#Diego Aspinwall
#11-20-17
#antsDemo.py - how to use lists with graphics

from ggame import *
from random import randint

WIDTH = 800
HEIGHT = 400
RAD = 10

if __name__ == '__main__':
    
    red = Color(0x660000,1)
    ant = CircleAsset(RAD,LineStyle(1,red),red)
    
    for i in range(0,10):
        Sprite(ant,(randint(RAD,WIDTH),randint(RAD,HEIGHT)))
    
    App().run()
