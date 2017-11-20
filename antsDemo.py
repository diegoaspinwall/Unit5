#Diego Aspinwall
#11-20-17
#antsDemo.py - how to use lists with graphics

from ggame import *
from random import randint

WIDTH = 800
HEIGHT = 400

if __name__ == '__main__':
    
    red = Color(0x660000,1)
    ant = CircleAsset(10,LineStyle(1,red),red)
    
    Sprite(ant,(randint(1,WIDTH),randint(1,WIDTH)))
    
    App().run()
