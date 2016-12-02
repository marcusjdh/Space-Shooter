"""
spaceshooter.py
Author: Marcus Helble
Credit: Wilson Rimberg

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
import ggame
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from random import random
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679



space_asset= ImageAsset("images/starfield.jpg",)
backg=Sprite(space_asset, (0,0))
backg2=Sprite(space_asset, (512,0))
backg3=Sprite(space_asset,(1024,0))
backg4=Sprite(space_asset, (0,512))
backg5=Sprite(space_asset, (512,512))
backg6=Sprite(space_asset, (1024, 512))
class SpaceShip(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1
        self.rx = 1
        self.ry = -1
        self.rxa = 0
        self.rxb = 0
        self.rya = 0
        self.ryb = 0
        self.c = 0
        self.d = 0
        self.visible = True
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.left)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.stopleft)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.right)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.stopright)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.up)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.stopup)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.down)
        SpaceGame.listenKeyEvent("keyup", "down arrow", self.stopdown)
        
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.rotation = 0
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
        if self.thrustframe == 4:
            self.thrustframe = 1
        

        else:
            self.setImage(0)

        if self.rxa == 2 and self.rxb == 2:
            self.x=self.x
            self.c = 0
        
        else:
            if self.rx == -5: 
                self.x=self.x-10
                self.c=1
            if self.rx == 5: 
                self.x=self.x+10
                self.c=2
      
            if self.rya == 2 and self.ryb == 2:
                self.y=self.y
                self.d = 0
            
            else: 
                if self.ry == -5: 
                    self.y=self.y-10
                    self.d = 1
                if self.ry == 5: 
                    self.y=self.y+10
                    self.d = 2
                if self.c==0 and self.d==0:
                    self.rotation = 0
                    self.thrust = 0
                else:
                    self.thrust=1
                    if self.c==1: 
                        if self.d==1:
                            self.rotation=(1/4)*pi
                    else:
                        if self.d==2: 
                            self.rotation=(3/4)*pi
                        else:
                            self.rotation=pi/2
                            if self.c==2: 
                                if self.d==1: 
                                    self.rotation=(7/4)*pi
                                else:
                                    if self.d==2: 
                                        self.rotation=(5/4)*pi
                                    else:
                                        self.rotation=(3/2)*pi
                                        if self.d==1: 
                                                 self.rotation=0
            
                                        if self.d==2: 
                                            self.rotation=pi
                                            collision = self.collidingWithSprites(Star)
                                            if len(collision) > 0:
                                                    self.visible=False
                                                    
    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0
    def left(self, event):
        self.rx=-5
        self.rxa=0
    def right(self, event):
        self.rx=5
        self.rxb=0
    def up(self, event):
        self.ry=-5
        self.rya=0
    def down(self, event):
        self.ry=5
        self.ryb=0
    def stopleft(self, event):
        self.rxa=2
    def stopright(self, event):
        self.rxb=2
    def stopup(self, event):
        self.ryb=2
    def stopdown(self, event):
        self.rya=2
    


class Star(Sprite):
   asset=ImageAsset("images/sun.png")
   height=300
   width=300

def __init__(self,im_num,position):
        super().__init__(Star.asset, position)
        self.setImage(im_num)
        Star(300,300)


        

    


class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/kSQdCxM.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg.scale = 0.6
        SpaceShip((125,100))
        SpaceShip((175,150))
        SpaceShip((75,150))
myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()