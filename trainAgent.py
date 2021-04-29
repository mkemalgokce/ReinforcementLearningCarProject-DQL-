from enviroment import Game
from agent import Agent
from car import Car

import numpy as np 
import cv2
import warnings 
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

TOTAL_TRAIN_TIME = 100000
IMGHEIGHT=40
IMGWIDTH=40
IMGHISTORY =4

def processGameImage(raw_image):
    raw_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
    raw_image = cv2.resize(raw_image,(40,40))
    raw_image = raw_image/255.0
    return raw_image

def TrainExperiment():
    
    TrainHistory = []
    
    game = Game()
    
    agent = Agent()
    
    BestAction = 0
    
    [InitialScore, InitialScreenImage] = game.play(BestAction)
    InitialGameImage = processGameImage(InitialScreenImage)

    GameState = np.stack((InitialGameImage,InitialGameImage,InitialGameImage,InitialGameImage),axis = 2)
    GameState = GameState.reshape(1, GameState.shape[0],GameState.shape[1],GameState.shape[2])

    for i in range(200):
        
        BestAction = agent.findBestWay(GameState)
        [ReturnScore, NewScreenImage] = game.play(BestAction)
        
        NewGameImage = processGameImage(NewScreenImage)
        
        NewGameImage = NewGameImage.reshape(1,NewGameImage.shape[0],NewGameImage.shape[1],1)
        
        NextState = np.append(NewGameImage, GameState[:,:,:,:3], axis = 3)
        
        agent.captureSample((GameState,BestAction,ReturnScore,NextState))
        
        agent.process()
        
        GameState = NextState
        
        if i % 250 == 0:
            print("Train time: ",i, " game score: ",game.GScore)
            TrainHistory.append(game.GScore)
    
TrainExperiment()