#Factores Primos
def  descomponer(n):
    facprimos=[]
    for i in range (2,n+1):
        while n % i ==0:
            facprimos.append(i)
            n=n/i
    return facprimos

h=int(input('ingrese un numero: '))
respuesta=descomponer(h)

for c in respuesta:
    print(c)      