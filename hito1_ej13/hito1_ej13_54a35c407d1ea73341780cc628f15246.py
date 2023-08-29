#Factores Primos
numero=int(input('ingresa un numero: '))
primos=[]
for i in range(2,numero+1):
    while numero%i==0:
        primos.append(i)
        numero=numero/i
i=0
while i<len(primos):
    print(primos[i])
    i=i+1
                 