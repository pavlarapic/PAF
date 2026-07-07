import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]
def histogram(podatci,k):
    data=sorted(podatci)
    x_min=data[0]
    x_max=data[-1]
    h=(x_max-x_min)/k
    rubovi=[x_min+i*h for i in range(k+1)]
    freq=[0]*k
    for d in data:
        for i in range(k):
            if i ==k-1:
                if rubovi[i] <=d<=rubovi[i+1]:
                    freq[i]+=1
                    break
            else:
                if rubovi[i] <=d<rubovi[i+1]:
                    freq[i]+=1
                    break
    for i in range(k):
        print(f"rubovi: [{rubovi[i]:.2f},{rubovi[i+1]:.2f}] frekvencija: {freq[i]}")
    return rubovi,freq
    
k_razreda=10

rubovi,frek=histogram(mase_ciste,k_razreda)

avg_razr=[]

for i in range(len(rubovi)-1):
    avg_razr.append((rubovi[i]+rubovi[i+1])/2)
width=rubovi[1]-rubovi[0]
plt.figure()
plt.bar(avg_razr,frek,width=width,alpha=0.4,color='blue')
plt.xlabel('Masa')
plt.ylabel('Frekvencija')
plt.title('Histogram')
plt.xticks(rubovi,rotation=45)
plt.show()
