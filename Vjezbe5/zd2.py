def sum(n):
    sum=0
    for _ in range(n):
        sum+=1/3
    a=5
    for _ in range(n):
        a-=1/3
    
    return sum,a


iteracije=[200,2000,20000]

for it in iteracije:
    suma=sum(it)
    print(suma)

#rezultat odstupa iz razloga koji je elaboriran u zd1.py
