import matplotlib.pyplot as plt
def jednoliko_gibanje(F,m,t,dt,v0=0,t0=0,x0=0):
    a = F / m
    vr_odmaci = []
    pomak = []
    brzina = []
    akc = []
    x = x0
    v = v0
    while t0 <= t:
        vr_odmaci.append(t0)
        pomak.append(x)
        brzina.append(v)
        akc.append(a)


        v = v + a*dt
        x = x + v*dt

        t0 = t0 + dt

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

