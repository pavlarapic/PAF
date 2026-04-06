import numpy as np
import matplotlib.pyplot as plt


class Particle:
    def __init__(self, v0,theta,x0,y0):
        self.v0=v0
        self.theta=np.radians(theta)
        self.x=x0
        self.y=y0
        self.g=9.81
        self.dt=0.001
        self.x_p=[]
        self.y_p=[]

    def reset(self):
        self.v0=None
        self.theta=None
        self.x=None
        self.y=None
        self.x_p=[]
        self.y_p=[]
        #doslovno briše sve o čestici
    def __move(self):
        vx=self.v0*np.cos(self.theta)
        vy=self.v0*np.sin(self.theta)
        self.x_p=[]
        self.y_p=[]
        while self.y>=0:
            self.x+=vx*self.dt
            self.y+=vy*self.dt
            vy-=self.g*self.dt
            self.x_p.append(self.x)
            self.y_p.append(self.y)

    def range(self):
        self.__move()
        return (self.x_p[-1])
    
    def plot_trajectory(self):
        self.__move()
        plt.plot(self.x_p, self.y_p,label='Numerički rezultati')
        plt.xlabel("x / m")
        plt.ylabel("y / m")
        plt.grid(True)
        plt.legend()
        plt.show()

