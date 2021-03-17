import numpy as np
import pygame as pg
import matplotlib.pyplot as plt
import simulator
import visualiser

objs = [
    simulator.Object(velocity=np.array([10,10]),dimensions=(0.5,0.5,1)),
    simulator.Object(velocity=np.array([0,10]),dimensions=(0.5,0.5,1)),
    simulator.Object(velocity=np.array([-5,10]),dimensions=(0.5,0.5,1)),
    simulator.Object(velocity=np.array([30,10]),dimensions=(0.5,0.5,1))
]

Engine = simulator.GEngine(objs,borders=(-10,-10,80,40),GravityConstent=3)

Engine.evolve(3)

p = np.array(Engine.Ob_list[0].pHistory)
v = np.array(Engine.Ob_list[0].vHistory)
t = np.array(Engine.tHistory)
#plt.scatter(p[:,0],p[:,1])
#plt.grid()
#plt.show()
#visualiser.Visualiser(Engine).visulize()

visualiser.plot(Engine.Ob_list[2],thistory=Engine.tHistory)
visualiser.plot(Engine.Ob_list[3],thistory=Engine.tHistory)

plt.show()