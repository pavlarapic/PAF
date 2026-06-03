import numpy as np 
import matplotlib.pyplot as plt 
h0 = 0.54 # m
m = 0.5257 # kg
r = 4.025e-3 # m
h_l = np.array([0.14 , 0.17 , 0.19 , 0.22 , 0.25 , 0.28 , 0.31 , 0.34 , 0.37 , 0.40]) # m
t_mean = np.array([1.740 , 1.793 , 2.043 , 2.190 , 2.280 , 2.417 , 2.540 , 2.640 , 2.670 , 2.813]) 
h=np.flip(h_l)
g=9.81
s=h0-h
log_t=np.log(t_mean)
log_s=np.log(s)

def lin_reg(x,y):
    n=len(x)
    br_a=n*np.sum(x*y)-np.sum(x)*np.sum(y)
    nz=n*np.sum(x**2)-(np.sum(x))**2
    a=br_a/nz 
    b=(np.sum(y)-a*np.sum(x))/(n)
    y_=a*x+b 
    diff = y -y_
    sigma_y=np.sqrt(np.sum(diff**2)/(n-2))
    sigma_a=sigma_y*np.sqrt(n/nz)
    sigma_b=sigma_y*np.sqrt(np.sum(x**2)/nz)
    return a,b,sigma_a,sigma_b 

a,b,sigma_a,sigma_b=lin_reg(log_t,log_s)

print(f"Za koeficijent a: {a:.5f}, pogreska: {sigma_a:.5f}")
print(f"Za koeficijent b: {b:.5f}, pogreska: {sigma_b:.5f}")

def lin_reg_O(x,y):
    n=len(x)
    a=np.sum(x*y)/np.sum(x**2)
    y_=a*x 
    diff=y-y_ 
    sigma_y=np.sqrt(np.sum(diff**2)/(n-1))
    sigma_a=sigma_y /np.sqrt(np.sum(x**2))
    return a,sigma_a 

x_t2=t_mean**2
y_s=h0-h 
a_t2,err_a_t2=lin_reg_O(x_t2,y_s)
print(f"Nagib pravca (a=a_ef/2):{a_t2:.5f}, greska: {err_a_t2:.5f}")

a_ef=2*a_t2 
err_a_ef= 2*err_a_t2 
Iz=m*(r**2)*((g/a_ef)-1)
err_Iz=((m*(r**2)*g)/(a_ef**2))*err_a_ef 
print(f"Efektivno ubrzanje a_ef:{a_ef:.5f}, greska: {err_a_ef:.5f}")
print(f"Moment tromosti:{Iz:.5f} greska: {err_Iz:.5f}")

plt.subplot(1,2,1)
plt.scatter(log_t,log_s,color='red',label='mjerenja')
plt.plot(log_t,a*log_t+b,label=f'Fit y={a:.5f}*log(t)+{b:.5f}')
plt.xlabel('$\\log(t)$')
plt.ylabel('$\\log(s)$')
plt.grid(True)
plt.legend(loc='upper left')
plt.subplot(1,2,2)
plt.scatter(x_t2,y_s,color='green',label='mjerenja')
plt.plot(x_t2,a_t2*x_t2,color='black',label=f'Fit kroz ishodište: y={-a_t2:.5f}x')
plt.xlabel('$t^2 /s^2$')
plt.ylabel('s/m')
plt.grid(True)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()





