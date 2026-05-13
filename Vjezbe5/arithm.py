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
    