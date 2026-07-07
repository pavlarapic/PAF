import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]
k=20

aritm_sr=np.mean(mase_ciste)
median=np.median(mase_ciste)

print(f"Aritmeticka sredina:{aritm_sr:.5f},medijan:{median:.5f}")
n, bins, patches = plt.hist(mase_ciste, bins=k, edgecolor='black', color='lightgreen', alpha=0.7, label='Histogram')
plt.axvline(aritm_sr, color='red', linestyle='dashed', linewidth=2, label=f'Aritmetička sredina ({aritm_sr:.5f})')
plt.axvline(median, color='blue', linestyle='dotted', linewidth=2, label=f'Medijan ({median:.5f})')

plt.xlabel('Masa')
plt.ylabel('Frekvencija')
plt.title('Histogram')
plt.legend()

plt.tight_layout()
plt.show()

print(f"Frekvencije u gotovom modulu:{n}")
