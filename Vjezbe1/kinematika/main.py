import kinematika

F = float(input("Unesite iznos sile u N: "))
m = float(input("Unesite iznos mase tijela u kg: "))
t = float(input("Unesite trajanje gibanja u s: "))
dt = 0.001
kinematika.jednoliko_gibanje(F,m,t,dt)