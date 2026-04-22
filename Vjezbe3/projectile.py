
import numpy as np
class Projectile:
    def __init__(self,theta,v0,x,y,dt,r,m,rho=1.225,g=9.81,C=0.47):
        self.theta=np.radians(theta)
        self.v0=v0
        self.x=x
        self.y=y
        self.g=g
        self.dt=dt
        self.C=C
        self.m=m
        self.r=r
        self.A=self.r**2*np.pi
        self.rho=rho
        self.x_p=[]
        self.y_p=[]
    def Euler(self):
        vx=self.v0*np.cos(self.theta)
        vy=self.v0*np.sin(self.theta)
        self.x_p=[self.x]
        self.y_p=[self.y]
        Fd = 0.5*self.rho*self.C*self.A
        while self.y_p[-1]>=0:
            v=np.sqrt(vx**2+vy**2)
            ax=(-Fd/self.m)*v*vx
            ay=-self.g-(Fd/self.m)*v*vy
            vx+=ax*self.dt
            vy+=ay*self.dt
            self.x_p.append(self.x_p[-1]+vx*self.dt)
            self.y_p.append(self.y_p[-1]+vy*self.dt)
        return np.array(self.x_p),np.array(self.y_p)
    def Runge_Kutta_4(self):
        vx=self.v0*np.cos(self.theta)
        vy=self.v0*np.sin(self.theta)
        self.x_p=[self.x]
        self.y_p=[self.y]
        Fd=0.5*self.rho*self.C*self.A
        while self.y_p[-1]>=0:
            def akc(vx_,vy_):
                v=np.sqrt(vx_**2+vy_**2)
                ax=(-Fd/self.m)*v*vx_
                ay=-self.g-(Fd/self.m)*v*vy_
                return ax,ay
            ax1,ay1=akc(vx,vy)
            ax2,ay2=akc(vx+ax1*self.dt/2,vy+ay1*self.dt/2)
            ax3,ay3=akc(vx+ax2*self.dt/2,vy+ay2*self.dt/2)
            ax4,ay4=akc(vx+ax3*self.dt/2,vy+ay3*self.dt/2)
            vx+=(self.dt/6)*(ax1+2*ax2+2*ax3+ax4)
            vy+=(self.dt/6)*(ay1+2*ay2+2*ay3+ay4)
            self.x_p.append(self.x_p[-1]+vx*self.dt)
            self.y_p.append(self.y_p[-1]+vy*self.dt)

        return np.array([self.x_p,self.y_p])