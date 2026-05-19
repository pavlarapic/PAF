from arithm import arithm
import numpy as np

# 5 mjerenja temperature vrenja vode [u stupnjevima Celzijusa]
malo_n = [99.8, 100.1, 99.9, 100.2, 100.0]
# 10000 mjerenja istog eksperimenta (simulacija)
np.random.seed(42)
veliko_n = np.random.normal(loc=100.0, scale=0.2, size=10000).tolist()

#copy-paste zadatka
#malo n
object_m_n=arithm(malo_n)
sr_object_m_n=object_m_n.aritm_sredina()
sigma_m_n=object_m_n.std_deviation1()
s_m_n=object_m_n.std_deviation2()
s_bar_m_n=object_m_n.std_deviation3()

rel_diff_m=(np.abs(sigma_m_n-s_m_n)/s_m_n)*100
#veliko n

object_v_n=arithm(veliko_n)
sr_object_v_n=object_v_n.aritm_sredina()
sigma_v_n=object_v_n.std_deviation1()
s_v_n=object_v_n.std_deviation2()
s_bar_v_n=object_v_n.std_deviation3()

rel_diff_v=(np.abs(sigma_v_n-s_v_n)/s_v_n)*100

print(f"Za mali skup podataka:")
print(f"Srednja vrijednost: {sr_object_m_n:.5f}\nSigma_n: {sigma_m_n:.5f}\ns: {s_m_n:.5f}\ns_bar: {s_bar_m_n:.5f}\nRelativna pogreska: {rel_diff_m:.5f}\n")
print("Za veci skup podataka:")
print(f"Srednja vrijednost: {sr_object_v_n:.5f}\nSigma_n: {sigma_v_n:.5f}\ns: {s_v_n:.5f}\ns_bar: {s_bar_v_n:.5f}\nRelativna pogreska: {rel_diff_v:.5f}")

#np.std je bolje koristiti za veci skup podataka, a to je ocito iz rezultata kada se kod pokrene

