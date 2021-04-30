'''
drawMap.py
Mustafa Kemal GOKCE
30.04.2021
You can draw map with this python file. If you want draw road, you can use 'd' key.
's' key saves file , 'a' key draws finish line and 'c' key clears screen.
'''
import pygame 
import numpy as np
import os
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MODE = 0

STARTPOINTX,STARTPOINTY =290,500
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Draw Levels')
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    running = True
    screen.fill((100,100,100))
    imgCount =0
    count = 0
    while running:
        pygame.draw.rect(screen,(0,255,0),(STARTPOINTX,STARTPOINTY,10,30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == 115: #S
                    print("Saving ...")
                    if(os.path.isfile('Assets/road'+str(imgCount)+'.bmp')):  #Save Screen
                        print("File Exists, please try again ...")
                        
                    else:
                        pygame.image.save(screen,'Assets/road'+str(imgCount)+'.bmp')
                    imgCount += 1
                if event.key == 99: #C
                    rewards = []
                    screen.fill((100,100,100)) #Clear Screen
                if event.key == 97 :# A
                    MODE = 1 # Draw Finish line
                if(event.key == 100): # D 
                    MODE = 0 # Draw Road
        click = pygame.mouse.get_pressed()
        mousex, mousey = pygame.mouse.get_pos()
        click = np.array(click)
        click = click[0],mousex,mousey
        if click[0]==True and MODE == 0:
            pygame.draw.rect(screen,(255,255,255),(click[1],click[2],40,40))

        if click[0]==True and MODE == 1:    
            pygame.draw.rect(screen,(0,255,0),(click[1],click[2],10,10))

        pygame.display.flip() 
    pygame.quit()
