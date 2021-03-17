import pygame
from os import sys
from pygame.locals import *
import simulator
import matplotlib.pyplot as plt
import numpy as np

pygame.init()
pygame.font.init()
class Visualiser():
    def __init__(self,Engine):
        self.engine = Engine
        self.screen_size = (600,600)
        self.px = 1 
        self.m = self.px * max(Engine.borders[2]/self.screen_size[0],
                        Engine.borders[3]/self.screen_size[0])
        self.speed = 1
        
    
    
    def visulize(self):
        self.screen = pygame.display.set_mode(self.screen_size)
        while 1:
            for i in range(len(self.engine.tHistory)):
                self.screen.fill((0,0,0))
                t = self.engine.tHistory
                try:
                    dt = self.engine.tHistory[i] - self.engine.tHistory[i-1]
                except:
                    dt = self.engine.tHistory[i] - self.engine.tHistory[i+1]
                for Obj in self.engine.Ob_list:
                    if Obj.shape == 'circle':
                        print(((Obj.pHistory[i][0]),(Obj.pHistory[i][1])),
                        int(Obj.radius/self.m))
                        pygame.draw.circle(self.screen,
                        (255,0,0),
                        (int(Obj.pHistory[i][0]/self.m-self.engine.borders[0]/self.m),
                            -int(Obj.pHistory[i][1]/self.m)+self.screen_size[1]+self.engine.borders[1]/self.m),
                        int(Obj.radius/self.m))
                    if Obj.shape == 'rectangle':
                        pygame.draw.rect(self.screen,
                        (255,0,0),
                        (int(Obj.pHistory[i][0]/self.m+self.engine.borders[0]/self.m),
                            int(Obj.pHistory[i][1]/self.m+self.screen_size[1]+self.engine.borders[1]/self.m),
                            int(Obj.length/self.m),
                            int(Obj.height/self.m)))
                pygame.display.update()
                pygame.time.delay(int(dt*1000))# ms


            
            
            
            for event in pygame.event.get():
                if event.type in (QUIT, KEYDOWN):
                    return 0
   
def plot(Obj, figure = None ,thistory = None,plot_insta_velocity=True, every=80,plot_mean_velocity=True):
    plt.figure(figure.number) if type(figure)!=type(None) else None 
    data=np.array(Obj.pHistory)
    print(len(data[:,1]))
    datav=np.array(Obj.vHistory)
    thistory=np.array(thistory)

    data2 = data[np.arange(0,len(data))%every==0]
    datav2= datav[np.arange(0,len(datav))%every==0]
    thistory2 = thistory[np.arange(0,len(thistory))%every==0]
    data3 = np.array([data2[:,0],data2[:,1]])
    datav3 = np.array([
        (data2[1:,0] - data2[:-1,0])/(thistory2[1:] - thistory2[:-1]),
        (data2[1:,1] - data2[:-1,1])/(thistory2[1:] - thistory2[:-1])
        ])
    
    plt.scatter(data2[:,0],data2[:,1],c='r')
    plt.quiver(*data3,datav2[:,0],datav2[:,1],scale = 80,width=0.005)
    plt.plot(data[:,0],data[:,1])


    
    plt.quiver(*data3[:,:-1],datav3[0],datav3[1],scale = 80,width=0.005,color="r")

        