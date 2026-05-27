import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]
mase=np.array(mase)

avg=np.mean(mase)
median=np.median(mase)
diff=abs(avg-median)

print(f"Aritmeticka sredina:{avg:.5f},medijan:{median:.5f},razlika:{diff:.5f}")

donja_gr=1.0
gornja_gr=3.0

mase_filtr=mase[(mase>=donja_gr)&(mase<=gornja_gr)]

avg_n=np.mean(mase_filtr)
median_n=np.median(mase_filtr)
diff_avg=abs(avg-avg_n)
diff_med=abs(median-median_n)

print(f"Nova aritmeticka sredina:{avg_n:.5f},novi medijan:{median_n:.5f}")
print(f"Razlika aritmetickih sredina:{diff_avg:.5f},razlika medijana:{diff_med:.5f}")

plt.hist(mase,bins=20,color='lightblue',edgecolor='black',alpha=0.6,label='Mjerenja')
plt.axvline(median,color='red',linestyle='--',label='Medijan mjerenja')
plt.axvline(avg,color='black',linestyle='--',label='Aritmeticka sredina mjerenja')
plt.axvline(avg_n,color='darkred',linestyle='--',label='Aritmeticka sredina filtriranih mjerenja')
plt.axvline(median_n,color='brown',linestyle='--',label='Medijan filtriranih mjerenja')

plt.title('Histogram i mjere srednjih vrijednosti')
plt.xlabel('Masa')
plt.ylabel('Frekvencija')
plt.legend()
plt.grid(axis='y',alpha=0.3)
plt.show()