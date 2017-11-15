#Diego Aspinwall
#10-13-17
#betterColoredWindow.py

from random import randint
from ggame import *

def mouseClick(event):
    colorlist = [Color(0xff0000, 1),Color(0x0000ff, 1),Color(0xffff00, 1),Color(0x00ff00, 1)]
    color = colorlist[randint(0,3)]
    rectangle = RectangleAsset(1000,1000,LineStyle(3,color),color)
    Sprite(rectangle)
App().listenMouseEvent('click', mouseClick)
App().run()

