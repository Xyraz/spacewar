import os
import random

#import turtle mode
import turtle
#Required by macosx to show the window
turtle.fd(0)
#set the animations speed to the maximum
turtle.speed(0)
#set the background to black
turtle.bgcolot("black")
#hide the default turtle
turtle.ht()
#this saves memory
turtle.setundobuffer(1)
#this speeds up drawing
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __init__(seld, spriteshape,color,startx,starty):
        turtle.Turtle.__init__(self,shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx,starty)
        self.speed= 1

    def move(self):
        self.fd(self.speed)

    class Player(Sprite):
        def __init__(seld, spriteshape,color,startx,starty):
        Sprite.__init__(self,shape=spriteshape,color,startz,starty)
        self.speed=4
        self.lives=3

player = Player("triangle","white", 0,0)

#game loop
while True:
    player.fd(player.speed)


delay = raw_input("Press enter to finish . >")