import numpy as np

class Calculus:
    def __init__(self,f):
        self.f = f
        self.n = 10000
    #privatne funkcije zadržavaju logiku deriviranja 
    #javne su fleksibilnije za korisnika
    #na način da on već u startu mora birati epsilon vrijednosti
    def __two_step(self,x,eps):
        return (self.f(x+eps)-self.f(x))/eps
    def __three_step(self,x,eps):
        return (self.f(x+eps)-self.f(x-eps)) /(2*eps)
    
    def derivacija_u_točki(self,x,eps,metoda="three-step"):
        if metoda=="two-step":
            return self.__two_step(x,eps)
        else:
            return self.__three_step(x,eps)
    
    def derivacija_na_intervalu(self,a,b,eps,metoda="three-step"):
        x_vr = np.linspace(a,b,self.n)
        deriv=[]
        for x in x_vr:
            if metoda == "two-step":
                deriv.append(self.__two_step(x,eps))
            else:
                deriv.append(self.__three_step(x,eps))
        return x_vr,deriv
    
    def riemann_integral(self,a,b,n):
        dx=(b-a)/n
        x=[a+i*dx for i in range(n+1)]
        lijeva_visina = [self.f(x[i]) for i in range(n)]
        desna_visina = [self.f(x[i+1]) for i in range(n)]
        l = sum(lijeva_visina) * dx
        d = sum(desna_visina) * dx
        p = {'x': x[:-1], 'lijeva_visina': lijeva_visina, 'desna_visina': desna_visina, 'dx': dx}
        return l,d,p
    
    def trapezna_formula(self,a,b,n):
        dx=(b-a)/n
        x=[a+i*dx for i in range(n+1)]
        suma=self.f(x[0])+self.f(x[n])
        for i in range(1, n):
            suma+=2*self.f(x[i])
        
        return (dx/2)*suma


