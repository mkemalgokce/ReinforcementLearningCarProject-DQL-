import pygame 
from pygame import draw,display,key
import math


STARTPOINTX,STARTPOINTY =290,500

class Car():
    def __init__(self):

        self.size = 40
        self.x = STARTPOINTX+17
        self.y = STARTPOINTY+20
        self.speed = 1
        self.maxSpeed = 2
        self.angle = 270
        self.acc = 0.1
        #init car
        self.surface = pygame.image.load('Assets/mycar.bmp')
        self.surface = pygame.transform.scale(self.surface, (self.size,self.size))
        self.rect = pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
        #Sensor Coordinates top part
        self.sensorCoordinates = [[0,0],[0,0],[0,0],[0,0],[0,0]]

    def resetCar(self):
        self.x = STARTPOINTX+17
        self.y = STARTPOINTY+20
        self.angle = 270
    def moveCar(self,action):
        
        self.speed += self.acc
        self.speed = min(self.maxSpeed,self.speed)
        self.x -= math.sin(math.radians(self.angle))*self.speed
        self.y -= math.cos(math.radians(self.angle))*self.speed
        self.rect = pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
        if action == 0 :
            self.addAngle(-3)
        elif action==1:
            self.addAngle(3)

    def addAngle(self,i):
        self.angle +=i
        self.angle = self.angle%360
    def computeDistance(self,a,b):     # It Computes distance between 2 points in coordinates system
        return math.sqrt((abs(b[0]-a[0])**2)+(abs(b[1]-a[1])**2))

    def updateSensors(self):
        #Front Sensor
        dx = (55*math.sin(math.radians(self.angle)))
        dy = (55*math.cos(math.radians(self.angle)))
        self.sensorCoordinates[0] =[self.x-dx,self.y-dy]
        #Right Sensor
        dx2 = (55*math.sin(math.radians(-30 + self.angle )))
        dy2 = (55*math.cos(math.radians(-30 + self.angle )))

        self.sensorCoordinates[1] =[self.x-dx2,self.y-dy2]
        #Left sensor
        dx1 = (55*math.sin(math.radians(30 + self.angle)))
        dy1 = (55*math.cos(math.radians(30 + self.angle)))

        self.sensorCoordinates[2] = [self.x-dx1,self.y-dy1]

                #Right Sensor
        dx3 = (40*math.sin(math.radians(-90 + self.angle )))
        dy3 = (40*math.cos(math.radians(-90 + self.angle )))

        self.sensorCoordinates[3] =[self.x-dx3,self.y-dy3]
        #Left sensor
        dx4 = (40*math.sin(math.radians(90 + self.angle)))
        dy4 = (40*math.cos(math.radians(90 + self.angle)))

        self.sensorCoordinates[4] =[self.x-dx4,self.y-dy4]
    def checkSensor(self,screen,switch):
        obsCoord = []

        color =(100,100,100)
        if(switch ==1):
            color = (0,255,0)
        #Sensor 0 -->Front : this part detects obstacles
        pixelX = int(self.x )
        pixelY = int(self.y)
        while self.computeDistance([pixelX,pixelY],[self.x,self.y]) <= self.computeDistance([self.x,self.y],self.sensorCoordinates[0]):
            if(screen.get_at((int(pixelX), int(pixelY)))[:3]==color):
                break
            pixelX-= math.sin(math.radians(self.angle))*1.1
            pixelY-= math.cos(math.radians(self.angle))*1.1
        obsCoord.append([pixelX,pixelY])
        #Sensor 1 -->Cross Right : this part detects obstacles
        pixelX = int(self.x )
        pixelY = int(self.y)
        while self.computeDistance([pixelX,pixelY],[self.x,self.y]) <= self.computeDistance([self.x,self.y],self.sensorCoordinates[1]):
            if(screen.get_at((int(pixelX), int(pixelY)))[:3]==color):
                break
            pixelX-= math.sin(math.radians(self.angle-30))*1
            pixelY-= math.cos(math.radians(self.angle-30))*1
        obsCoord.append([pixelX,pixelY])
        #Sensor 2 -->Cross Left : this part detects obstacles
        pixelX = int(self.x )
        pixelY = int(self.y)
        while self.computeDistance([pixelX,pixelY],[self.x,self.y]) <= self.computeDistance([self.x,self.y],self.sensorCoordinates[2]):
            if(screen.get_at((int(pixelX), int(pixelY)))[:3]==color):
                break
            
            pixelX-= math.sin(math.radians(self.angle+30))*1
            pixelY-= math.cos(math.radians(self.angle+30))*1
        obsCoord.append([pixelX,pixelY])
        #Sensor 3 -->Right : this part detects obstacles
        pixelX = int(self.x )
        pixelY = int(self.y)
        while self.computeDistance([pixelX,pixelY],[self.x,self.y]) <= self.computeDistance([self.x,self.y],self.sensorCoordinates[3]):
            if(screen.get_at((int(pixelX), int(pixelY)))[:3]==color):
                break
            
            pixelX-= math.sin(math.radians(self.angle-90))*1
            pixelY-= math.cos(math.radians(self.angle-90))*1
        obsCoord.append([pixelX,pixelY])
        #Sensor 4 -->Left : this part detects obstacles
        pixelX = int(self.x )
        pixelY = int(self.y)
        while self.computeDistance([pixelX,pixelY],[self.x,self.y]) <= self.computeDistance([self.x,self.y],self.sensorCoordinates[4]):
            if(screen.get_at((int(pixelX), int(pixelY)))[:3]==color):
                break
            
            pixelX-= math.sin(math.radians(self.angle+90))*1
            pixelY-= math.cos(math.radians(self.angle+90))*1
        obsCoord.append([pixelX,pixelY])

        if(switch == 0):
            #Draw Obstacle Rectangles
            #Sensor 0 -->Front
            pygame.draw.rect(screen,(255,255,0),[obsCoord[0][0],obsCoord[0][1],8,8])
            #Sensor 1 -->Cross Right
            pygame.draw.rect(screen,(255,0,255),[obsCoord[1][0],obsCoord[1][1],8,8])
            #Sensor 2 -->Cross Left
            pygame.draw.rect(screen,(0,0,255),[obsCoord[2][0],obsCoord[2][1],8,8])
            #Sensor 3 -->Right
            pygame.draw.rect(screen,(255,0,0),[obsCoord[3][0],obsCoord[3][1],8,8])
            #Sensor 4 -->Left
            pygame.draw.rect(screen,(20,100,0),[obsCoord[4][0],obsCoord[4][1],8,8])

        valFront = self.computeDistance([obsCoord[0][0],obsCoord[0][1]],[self.x,self.y])/self.computeDistance([self.x,self.y],self.sensorCoordinates[0])
        valcRight = self.computeDistance([obsCoord[1][0],obsCoord[1][1]],[self.x,self.y])/self.computeDistance([self.x,self.y],self.sensorCoordinates[1])
        valcLeft =  self.computeDistance([obsCoord[2][0],obsCoord[2][1]],[self.x,self.y])/self.computeDistance([self.x,self.y],self.sensorCoordinates[2])
        valRight =   self.computeDistance([obsCoord[3][0],obsCoord[3][1]],[self.x,self.y])/self.computeDistance([self.x,self.y],self.sensorCoordinates[3])
        valLeft = self.computeDistance([obsCoord[4][0],obsCoord[4][1]],[self.x,self.y])/self.computeDistance([self.x,self.y],self.sensorCoordinates[4])

        
    
        return valFront,valcRight,valcLeft,valRight,valLeft