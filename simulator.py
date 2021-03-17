import numpy as np
class Object():
    def __init__(self,shape='circle',dimensions=(0.5,0.5,0.1),velocity=(0,0)):
        self.shape=shape
        self.position = np.array([dimensions[0],dimensions[1]])
        self.velocity = np.array([velocity[0],velocity[1]])
        
        if self.shape=='circle':
            self.radius = dimensions[2]
        
        elif self.shape=='rectangle':
            self.length = dimensions[2]
            self.height  = dimensions[3]
            try:
                self.oriontation = dimensions[4]
            except:
                self.oriontation = 0

        elif self.shape=='triangle':
            self.base = dimensions[2]
            self.hight  = dimensions[3]
            try:
                self.oriontation = dimensions[4]
            except:
                self.oriontation = 0
        
        else:
            raise SystemError

        self.pHistory = [self.position]
        self.vHistory = [self.velocity]
    
    def set_system(self,position=None,velocity= None):
        self.position = (np.array(position) if not(type(position)==None) else self.position)
        self.velocity = (np.array(velocity) if not(type(velocity)==None) else self.velocity)
        self.archieve()

    def archieve(self):
        self.pHistory.append(self.position)
        self.vHistory.append(self.velocity)


class GEngine():
    def __init__(self,ObjectsList,GravityConstent=10,borders=(0,0,1,1),dt= 0.01):
        self.G = GravityConstent
        self.borders=borders
        self.Ob_list= ObjectsList  
        self.tHistory =  [0] 
        self.dt = dt  
        self.t = 0   

    def evolve(self,to_time):
        N = int((to_time-self.t)/self.dt)
        for i in range(1,N+1):
            for j in range(len(self.Ob_list)):
                self.evolve_object(j)
            self.t+=self.dt
            self.tHistory.append(self.t)
        
        if self.t != to_time:
            for j in range(len(self.Ob_list)):
                print(to_time-self.t)
                self.evolve_object(j,to_time-self.t)
            self.t=to_time
            self.tHistory.append(self.t)

    
    def next_position(self,object,dt):
            return np.array([object.position[0]+object.velocity[0]*dt,-1/2 *self.G * dt*dt + object.velocity[1] * dt + object.position[1]])
    
    def next_velocity(self,object,dt):
            return np.array([object.velocity[0], -self.G * dt + object.velocity[1]])

    def evolve_object(self,i_object,dt= None):
        dt = dt if dt!= None else self.dt
        Obj = self.Ob_list[i_object]
        Obj.set_system(
            self.next_position(Obj,dt),
            self.next_velocity(Obj,dt)
        )
