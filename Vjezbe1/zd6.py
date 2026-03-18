import matplotlib.pyplot as plt
import numpy as np

F = float(input("Unesite iznos sile u N: "))
m = float(input("Unesite masu čestice u kg: "))

#Odaberimo proizvoljan diferencijal vremena dovoljno malen da se izbjegnu pogreške prilikom aproksimacija
#ali dovoljno velik da ne bude prevelikog odstupanja od uobičajne integracijske metode

#s obzirom na gornje uvjete, neka je dt = 0.001 s 

dt = 0.001


#iz cinjenice o II. NZ-u, zbog toga sto na tijelo djeluje sila, ono ima konstantnu akceleraciju.

a = F / m

'''
budući da ne možemo direktno uzimati vrijednosti iz gotovih formula jer zadatak inzistira na numeričkom rješavanju, koristim Eulerovu metodu aproksimacije

Postavljam početne podatke u trentuku t1 = 0 s
'''
x = 0
v = 0
t = 0 #zamjena varijable t1 sa t da bude preglednije, u suštini isto je samo je prilagođeno programskom jeziku


#od toga t = 0 gledam svaki dt do t = 10 koristeći while petlju

#nadalje, zbog plota kreirati ću 4 liste koje ce biti nužne da se podatci uopće prikažu grafički
#isto tako te liste će primati svaki član koji ovisi o dt-u odnosno pridodaje im odgovarajuće dv i dx

vr_odmaci = []
pomak = []
brzina = []
akc = []

while t <=10:
    vr_odmaci.append(t)
    pomak.append(x)
    brzina.append(v)
    akc.append(a)


    v = v + a*dt
    x = x + v*dt

    t = t + dt

plt.figure()
plt.plot(vr_odmaci,pomak)
plt.title("x-t graf")
plt.xlabel("t / [s]")
plt.ylabel("x / [m]")
plt.grid(True)

plt.figure()
plt.plot(vr_odmaci,brzina)
plt.title("v-t graf")
plt.xlabel("t / [s]")
plt.ylabel("v / [m/s]")
plt.grid(True)

plt.figure()
plt.plot(vr_odmaci,akc)
plt.title("a-t graf")
plt.xlabel("t / [s]")
plt.ylabel("a / [m/s^2]")
plt.grid("True")

plt.show()