#program isto radi samo za brojeve iz N

def pravac(x1,y1,x2,y2):
    if x1 == x2: #ovo je slučaj ako je vertikalan kao i 'gateway' za dijeljenje s 0 u nastavku koda
        print(f"Jednadzba pravca je x={x1}")
    else:
        k = (y2 - y1) / (x2 - x1)
        l = y1 - k * x1
        print(f"Jednadžba pravca je: y = {k}x + {l}")
    
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

pravac(x1,y1,x2,y2)
