import numpy as np

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]

def median(podatci):
    data=sorted(podatci)
    x_min=data[0]
    x_max=data[-1]
    n=len(data)
    if n % 2==0:
        idx1=(n//2)-1
        idx2=n//2
        x_bar=(data[idx1]+data[idx2]) /2
    else:
        idx=n//2
        x_bar=data[idx]
    return x_bar

a = [3, 1, 4, 1, 5, 9, 2, 6]
b = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print(f"Za listu a:{median(a)}")
print(f"Za b listu:{median(b)}")

my_modulus=median(mase)
numpy_res=np.median(mase)

print(f"Moj rezultat:{my_modulus:.5f}, numpy:{numpy_res:.5f}")
