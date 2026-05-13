import numpy as np
from arithm import arithm

data = [1,2,3,4,5,6,7,8,9,10]
analysis=arithm(data)
print(f"Aritmeticka sredina:{analysis.aritm_sredina()}")
print(f"Standardna devijacija: {analysis.standard_deviation()}")


def numpy_method(data):
        sredina=np.mean(data)
        deviation=np.std(data,ddof=1)/np.sqrt(len(data))
        return deviation, sredina

sredina_np,deviation_np=numpy_method(data)

print(f"Numpy aritmeticka sredina: {sredina_np}")
print(f"Numpy devijacija: {deviation_np}")