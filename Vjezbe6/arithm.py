#program generalno funkcionira za sve vrijednosti
import numpy as np

class arithm:
    def __init__(self,data):
        self.data=data
        self.n=len(self.data)

    def __sum__(self):
        sum=0
        for d in self.data:
            sum+=d
        return sum
    
    def aritm_sredina(self):
        x_sum=self.__sum__()
        x_bar=x_sum/(self.n)
        return x_bar

    def __brojnik__(self):
        sum=0
        x_bar=self.aritm_sredina()
        for d in self.data:
            sum +=(d-x_bar)**2
        return sum

    def standard_deviation(self):
        b=self.__brojnik__()
        sigma=np.sqrt(b/(self.n*(self.n-1)))
        return sigma
    

    #nadalje prosirujem modul konkretno za ove vjezbe
    #dodajem formule 4 i 7
    #razlog tome je funkcionalnost i lakse debugganje ukoliko nesto krene po krivu

    #formula 4
    def __partial_derivation__(self,func,variables,index,h=1e-5):
        v_plus=list(variables)
        v_minus=list(variables)
        v_plus[index]+=h
        v_minus[index]-=h
        derivation=(func(*v_plus)-func(*v_minus))/(2*h)
        return derivation
    
    #source ovoga je wikipedija link: https://en.wikipedia.org/wiki/Partial_derivative
    #stavka odakle sam ovo izvukla je Definition
    #ovaj 1e-5 je 10^{-5} radi preciznosti 

    def propagation(self, func, variables, sigmas):
        sum_err=0

        for i in range(len(variables)):
            df_dxi=self.__partial_derivation__(func,variables,i)
            err=(df_dxi*sigmas[i])**2
            sum_err+=err
            sigma_f=np.sqrt(sum_err)
            return sigma_f
    #ovdje je cista implementacija __partial_derivative__ uz nastavak formule

    #dalje samo povlacim vec definirane stavke iz arithm.py

    def std_deviation1(self):
        b=self.__brojnik__()
        sigma_n=np.sqrt(b/self.n)
        return sigma_n
    
    def std_deviation2(self):
        b=self.__brojnik__()
        np.sqrt(b/(self.n-1))
        return np.sqrt(b/(self.n-1))
    
    def std_deviation3(self):
        s=self.std_deviation2()
        return s/(np.sqrt(self.n))
    