import pygame 
from pygame import draw,display,key
import math

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
MODE = 1
STARTPOINTX= 250
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption('Car Game')

    def run(self):
        pass



class Car:
    def __init__(self):
        self.x = STARTPOINTX
        self.y = SCREEN_HEIGHT-50
        
        self.size = 30
        self.speed = 1
        self.maxSpeed = 1.2
        self.angle = 0 
        self.acc = 0.2
        #init car
        self.surface = pygame.image.load('Assets/mycar.png')
        self.rect = pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
        #Sensor Coordinates top part
        self.sensorCoordinates = [[0,0],[0,0],[0,0]]

    def speedUp(self):  
        self.speed += self.acc
        self.speed = min(self.maxSpeed,self.speed)
        self.x -= math.sin(math.radians(self.angle))*self.speed
        self.y -= math.cos(math.radians(self.angle))*self.speed
        self.rect = pygame.Rect(self.x-self.size[0]/2,self.y-self.size[1]/2,self.size[0],self.size[1])

    def steerRight(self):
        self.addAngle(-3)
    def steerLeft(self):
        self.addAngle(3)
    def addAngle(self,i):
        self.angle +=i
        self.angle = self.angle%360
    def speedDown(self):
        self.speed -= self.acc
        self.speed = max(1,self.speed)
        self.x += math.sin(math.radians(self.angle))*self.speed
        self.y += math.cos(math.radians(self.angle))*self.speed
        self.rect = pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
    def computeDistance(self,a,b):     # It Computes distance between 2 points in coordinates system
        return math.sqrt((abs(b[0]-a[0])**2)+(abs(b[1]-a[1])**2))

car = Car()