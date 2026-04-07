from calculus import Calculus
import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return x**3

def af1(x):
    return 3*x**2

def f2(x):
    return np.sin(x)

def af2(x):
    return np.cos(x)


c1 = Calculus(f1)

x1,d2 = c1.derivacija_na_intervalu(-5,5,eps=0.0001,metoda="two-step")
x1_,d3 = c1.derivacija_na_intervalu(-5,5,eps=0.0001,metoda="three-step")

c2 = Calculus(f2)
x2,d2_=c2.derivacija_na_intervalu(0,2*np.pi,eps=0.001,metoda="two-step")
x2_,d3_=c2.derivacija_na_intervalu(0,2*np.pi,eps=0.01,metoda="three-step")
analiticki2=np.linspace(0,2*np.pi,100)
d2_analitcki=af2(analiticki2)
analiticki=np.linspace(-5,5.100)
d_analiticki=af1(analiticki)

plt.figure()
plt.title("Derivacija kubne funkcije")
plt.plot(analiticki,d_analiticki,'--',alpha=0.7,color='black',label="Analitička derivacija")
plt.plot(x1,d2,'-.',alpha=0.4,color='red',label="Metoda 'two-step'")
plt.plot(x1_,d3,'-',alpha=0.5,color='orange',label="Metoda 'three-step'")
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.title("Derivacija sinusne funkcije")
plt.plot(analiticki2,d2_analitcki,'--',alpha=0.7,color='black',label='Analiticka derivacija sinusa')
plt.plot(x2,d2_,'-.',alpha=0.4,color='red',label="Metoda 'two-step'")
plt.plot(x2_,d3_,'-',alpha=0.5,color='orange',label="Metoda 'three-step'")
plt.grid(True)
plt.legend()
plt.show()