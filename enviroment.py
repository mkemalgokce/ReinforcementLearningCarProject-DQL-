import pygame 
from pygame import draw,display,key
import math
from car import Car
import os
from agent import DQLAgent
import numpy as np
os.environ['KMP_DUPLICATE_LIB_OK']='True'
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FPS = 60
x = 0
y = 0

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption("Car Game")
        self.agent = DQLAgent()
        self.car = Car()
        self.clock = pygame.time.Clock()
        self.vals = [0,0,0,0,0]
        self.reward = 0
        self.totalReward = 0.0
        self.done = False
        self.level = 0
        self.loadLevel(self.level)

        
    def loadLevel(self, level):
        if(os.path.isfile('Assets/road'+str(level)+'.bmp')):
            self.map = pygame.image.load(r'Assets/road'+str(level)+'.bmp')
        else:
            print('Resim bulunamadi. Default map aciliyor...')
            self.map = pygame.image.load(r'Assets/road'+str(0)+'.bmp')
    def initialDisplay(self):
        self.vals = [0,0,0,0,0]
        self.reward = 0
        self.totalReward = 0.0
        self.done = False
        self.car.resetCar()
        self.loadLevel(self.level)
        state = self.drawCar()
        self.loadRoad()
        return state
    def drawCar(self):
        global x,y
        rot = pygame.transform.rotate(self.car.surface, self.car.angle)
        new_rect = rot.get_rect(center = self.car.surface.get_rect(center = (self.car.x, self.car.y)).center)
        #Draw sensors
        self.car.updateSensors()
        # Get distance values
        vals = self.car.checkSensor(self.screen,0)
        rewardVals = self.car.checkSensor(self.screen,1)
        if(self.isCollide(vals)):
            x=0
            y=0
            self.done = True
        if(self.isCollide(rewardVals)):
            x = self.car.x
            y = self.car.y
            self.level+=1
            self.initialDisplay()

        #Front sensor
        pygame.draw.line(self.screen,(0,255,255),(self.car.x,self.car.y),(self.car.sensorCoordinates[0]),2)
        #CrossRight sensor
        pygame.draw.line(self.screen,(0,255,255),(self.car.x,self.car.y),(self.car.sensorCoordinates[1]),2)
        #Cross Left sensor
        pygame.draw.line(self.screen,(0,255,255),(self.car.x,self.car.y),(self.car.sensorCoordinates[2]),2)
        #Right
        pygame.draw.line(self.screen,(0,255,255),(self.car.x,self.car.y),(self.car.sensorCoordinates[3]),2)
        #Left sensor
        pygame.draw.line(self.screen,(0,255,255),(self.car.x,self.car.y),(self.car.sensorCoordinates[4]),2)

        self.vals = vals
        self.screen.blit(rot,new_rect)
        return self.vals

    def isCollide(self,vals):
        if min(vals)<0.2 :
            return True
        else :
            return False
    def loadRoad(self):
        self.screen.blit(self.map, (0, 0))

    def play(self,action):
        pygame.event.pump()
        self.loadRoad()
        self.car.moveCar(action)
        vals = self.drawCar()
        return vals
    
    def run(self):
        state = self.initialDisplay()
        running = True
        while running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return False
            # action = 2
            # keys=pygame.key.get_pressed()
            # if keys[pygame.K_UP]:
            #     action = 2
            # if keys[pygame.K_RIGHT]:

            #     action = 0
            # if keys[pygame.K_LEFT]:
            #     action = 1
            # self.play(action)
            self.reward += 1
            if(self.done == True):
                self.reward -= 100
                self.totalReward += self.reward
                print("Total Reward :",self.totalReward)
                running=False
            action = self.agent.act(state)
            if(action == 0):
                 print("RIGHT")
            elif action ==1 :
                print("LEFT")
            self.play(action)
            next_state = self.play(int(action))
            self.agent.remember(state,action,self.reward,next_state,self.done)
            state = next_state
            self.agent.replay(9)
            self.agent.adaptiveEGreedy()
            pygame.display.flip() 
            
if __name__ == "__main__":
    env = Game()
    t = 0
    running = True
    while running:
        t += 1
        print("Train: ",t)      
        # initialize pygame and create window
        pygame.display.set_caption("RL Car Game")
        clock = pygame.time.Clock()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            break
        
        if (env.run() == False):
            running = False
    pygame.quit()

