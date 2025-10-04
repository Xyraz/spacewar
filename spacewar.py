import os
import random

import turtle
turtle.fd(0)
turtle.speed(0)
turtle.bgcolot("black")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __init__(seld, spriteshape,color,startx,starty):
        turtle.Turtle.__init__(self,shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx,starty)
        self.speed=1

delay = raw_input("Press enter to finish . >")