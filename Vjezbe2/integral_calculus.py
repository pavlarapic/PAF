import matplotlib.pyplot as plt
from calculus import Calculus

def f(x):
    return x**2

calc=Calculus(f)
a,b=0,10
analiticko = (b**3-a**3)/3
n_vr = [5, 10, 50, 100]
l_vr = []
d_vr = []
t_vr = []
for n in n_vr:
    l,d,_ = calc.riemann_integral(a,b,n)
    t = calc.trapezna_formula(a,b,n)
    l_vr.append(l)
    d_vr.append(d)
    t_vr.append(t)

plt.plot(n_vr, l_vr, marker='o', label='Lijeva Riemannova suma')
plt.plot(n_vr, d_vr, marker='s', label='Desna Riemannova suma')
plt.plot(n_vr, t_vr, marker='^', label='Trapezna formula')
plt.axhline(analiticko,linestyle='--',label='Analiticko rjesenje')
plt.xlabel('Broj podintervala n')
plt.ylabel('Vrijednost integrala')
plt.title('Usporedba numerickih integracija')
plt.legend()
plt.grid(True)
plt.show()