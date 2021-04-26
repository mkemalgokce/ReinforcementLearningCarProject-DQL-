import pygame 
from pygame import draw,display,key
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
MODE = 1
STARTPOINTX= 250
FPS = 60


class Car:
    def __init__(self):
        self.x = STARTPOINTX
        self.y = SCREEN_HEIGHT-50
        
        self.size = 30
        self.speed = 0.4
        self.maxSpeed = 1.2
        self.angle = 0 
        self.acc = 0.2
        #init car
        self.surface = pygame.image.load('Assets/mycar.png')
        self.rect = pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
        #Sensor Coordinates top part
        self.sensorCoordinates = [[0,0],[0,0],[0,0]]

    def updateCar(self,action):
        if(action=='up'):
            self.speed += self.acc
            self.speed = min(self.maxSpeed,self.speed)
            self.x -= math.sin(math.radians(self.angle))*self.speed
            self.y -= math.cos(math.radians(self.angle))*self.speed
            self.rect = pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
        elif(action=='down'):
            self.speed -= self.acc
            self.speed = max(1,self.speed)
            self.x += math.sin(math.radians(self.angle))*self.speed
            self.y += math.cos(math.radians(self.angle))*self.speed
            self.rect = pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
        elif(action=='right'):
            self.addAngle(-3)
            
        elif(action=='left'):
            self.addAngle(3)
    def addAngle(self,i):
        self.angle +=i
        self.angle = self.angle%360
    def computeDistance(self,a,b):     # It Computes distance between 2 points in coordinates system
        return math.sqrt((abs(b[0]-a[0])**2)+(abs(b[1]-a[1])**2))


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Car Project')
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.car = Car()
        print('car')
        self.clock = pygame.time.Clock()
        self.initialDisplay()
        self.run()
        
    def initialDisplay(self):
        pygame.event.pump()
        self.screen.fill((255,255,255))
        self.drawCar()
    def drawCar(self):
        rot = pygame.transform.rotate(self.car.surface, self.car.angle)
        new_rect = rot.get_rect(center = self.car.surface.get_rect(center = (self.car.x, self.car.y)).center)
        self.screen.blit(rot,new_rect)
        
    def loadRoad(self,switch:int):
        pass

    def play(self):
        pygame.event.pump()

        score = 0
        
        self.screen.fill((255,255,255)) #WHITE
        #self.car.updateCar(action)
        self.drawRoad()
        self.drawCar()
    def run(self):
        running = True
        while running:
            self.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            pygame.display.flip() 
        pygame.quit()
a = Game()