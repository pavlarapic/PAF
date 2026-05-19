diameter={
    "v1":[19.98,20.18,20.10,20.08,19.74],
    "v2":[19.92,19.82,19.96,19.98,19.88],
    "v3":[24.96,24.98,24.92,24.94]
}

length={
    "v1":[49.80,49.00,50.48,49.80,49.96],
    "v2":[52.56,52.50,52.62,52.58,52.54],
    "v3":[55.34,55.40,55.30,55.44,55.48]
}
mass={
    "v1":[138.92, 138.98, 139.20, 138.90, 138.92],
    "v2":[128.65, 128.60, 128.65, 128.35, 128.50],
    "v3":[ 71.89, 71.90, 71.79, 71.85, 71.70]
}

from arithm import arithm
import numpy as np


def volumen_valjka(R,L):
    return np.pi*(R**2)*L

def sigma_volumen(R,sigma_R,L,sigma_V):
    calc=arithm([])
    return calc.propagation(volumen_valjka, [R,L],[sigma_R,sigma_L])

def gustoca_valjka(M,R,L):
    rho = M/volumen_valjka(R,L)
    return rho

def sigma_gust(M,sigma_M,R,sigma_R,L,sigma_L):
    calc=arithm([])
    values=[M,R,L]
    err=[sigma_M,sigma_R,sigma_L]
    return calc.propagation(gustoca_valjka,values,err)

literatura={
    "v1":{"material":"Cu", "rho_li":8.96},
    "v2":{"material":"Fe", "rho_li":7.85},
    "v3":{"material":"Al", "rho_li":2.7}
}

def rel_pogr(rho_calculated,rho_lit):
    odstupanje=(np.abs(rho_calculated-rho_lit)/rho_lit) *100
    return odstupanje

for valjak in ["v1","v2","v3"]:
    radius=[d/20.0 for d in diameter[valjak]]
    arithm_R=arithm(radius)
    R_sr=arithm_R.aritm_sredina()
    sigma_R=arithm_R.standard_deviation()
    
    leng=[l/10.0 for l in length[valjak]]
    L=arithm(leng)
    L_sr=L.aritm_sredina()
    sigma_L=L.standard_deviation()

    M=arithm(mass[valjak])
    M_sr=M.aritm_sredina()
    sigma_M=M.standard_deviation()

    V_sr=volumen_valjka(R_sr,L_sr)
    sigma_V=sigma_volumen(R_sr,sigma_R,L_sr,sigma_L)

    rho_sr=gustoca_valjka(M_sr,R_sr,L_sr)
    sigma_rho=sigma_gust(M_sr,sigma_M,R_sr,sigma_R, L_sr,sigma_L)

    rho_lit_valjka = literatura[valjak]["rho_li"]
    the_material = literatura[valjak]["material"]

    delta_rho=rel_pogr(rho_sr,rho_lit_valjka)

    print(f"Rezultat za valjak: {valjak.upper()}")
    print(f"R = {R_sr:.5e} +/- {sigma_R:.5e}")
    print(f"L = {L_sr:.5e} +/- {sigma_L:.5e}")
    print(f"V = {V_sr:.5e} +/- {sigma_V:.5e}")
    print(f"Gustoca: rho = {rho_sr:.5e} +/- {sigma_rho:.5e}")
    print(f"Relativna pogreska: delta_rho={delta_rho:.5f}%\n")#\n radi preglednosti
