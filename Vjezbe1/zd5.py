#uzeti ću kod iz prethodnog zadatka i proširiti ga

import matplotlib.pyplot as plt 

#iz svog 4.zadatka: 


#program isto radi samo za brojeve iz N

def pravac(x1,y1,x2,y2):
    if x1 == x2: #ovo je slučaj ako je vertikalan kao i 'gateway' za dijeljenje s 0 u nastavku koda
        print(f"Jednadzba pravca je x={x1}")
    else:
        k = (y2 - y1) / (x2 - x1)
        l = y1 - k * x1
        print(f"Jednadžba pravca je: y = {k}x + {l}")
        return k,l #ovo mi je potrebno kako bi donji dio koda radio
    #odnosno da nemam ovoga returna, ostatak koda nema smisla jer nemam spremljene vrijednosti 

while True:
    x1 = input("Unesite x koordinatu prve točke: ")
    y1 = input("Unesite y koordinatu prve točke: ")
    x2 = input("Unesite x koordinatu druge točke: ")
    y2 = input("Unesite y koordinatu druge točke: ")


#iduci set linija ispituje je li unos ispravan i konvertira ga u int 

    if not x1.isdigit() or not x2.isdigit() or not y1.isdigit() or not y2.isdigit():
        print("Pogrešan unos. Unesite ispravne koordinate")
        continue
    else:
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        break

k,l = pravac(x1,y1,x2,y2)

def prikazi_spremi(x1,y1,x2,y2):
    plt.figure()
    plt.scatter([x1,x2], [y1,y2],color='blue',label='Točke')

    if x1 == x2:
        plt.axvline(x=x1, color='blue', label='Pravac')

    else:
        x_min, x_max = min(x1,x2) -1, max(x1,x2) +1
        x_vrijednosti = [x_min,x_max]
        y_vrijednosti = [k*x + l for x in x_vrijednosti]
        plt.plot(x_vrijednosti,y_vrijednosti,color='blue',label='Pravac')

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Pravac kroz dvije točke")
    plt.legend()
    plt.grid(True)

    while True:
        opcije = input("Za prikaz grafa unesite 'p', za spremanje 's': ").strip().lower()
        if opcije == 'p':
            plt.show()
            break
        elif opcije == 's':
            ime = input("Unesite ime datoteke bez ekstenzije: ").strip()
            plt.savefig(f"{ime}.pdf")
            print(f"Graf je uspješno spremljen kao {ime}.pdf")
            break
        else:
            print("Odaberite 'p' za prikaz ili 's' za spremanje: ")
            continue
        #u principu ovdje inzistiram da se odaberu opcije.

prikazi_spremi(x1,y1,x2,y2)

