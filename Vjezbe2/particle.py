import numpy as np
import matplotlib.pyplot as plt 
class Particle:
    def __init__(self,v0, theta, x0,y0):
        self.v0 = v0
        self.theta = np.radians(theta)
        self.x = x0
        self.y = y0
        self.g = 9.81
        self.dt = 0.001
        self.x_lista = []
        self.y_lista = []

    def printInfo (self):
        print(self.v0,self.theta,self.x,self.y)
    
    def reset(self):
        self.v0 = None
        self.theta = None
        self.x = None
        self.y = None
        self.x_lista = []
        self.y_lista = []

    def __move(self):
        vx = self.v0 *np.cos(self.theta)
        vy = self.v0 * np.sin(self.theta)
        self.x += vx *self.dt
        self.y += vy * self.dt -0.5 * self.g *self.dt**2
        self.v0 = np.sqrt(vx**2 + (vy -self.g*self.dt**2)**2)
        print(self.x,self.y,self.v0)
        
    def range(self):
        x = self.x
        y = self.y
        vx = self.v0 *np.cos(self.theta)
        vy = self.v0 *np.sin(self.theta)
        while y >= 0:
            x += vx *self.dt
            y += vy*self.dt -0.5 *self.g *self.dt**2
            vy -= self.g *self.dt
        return x
    
    def plot_trajectory(self):
        x = self.x
        y = self.y
        vx = self.v0 *np.cos(self.theta)
        vy = self.v0 *np.sin(self.theta)
        self.x_lista = [x]
        self.y_lista =[y]
        while y >= 0:
            x += vx*self.dt
            y += vy*self.dt
            vy -= self.g*self.dt
            self.x_lista.append(x)
            self.y_lista.append(y)

        plt.plot(self.x_lista,self.y_lista)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Putanja projektila")
        plt.grid(True)
        plt.show()
        
p = Particle(20, 45, 0, 0)
p.plot_trajectory()