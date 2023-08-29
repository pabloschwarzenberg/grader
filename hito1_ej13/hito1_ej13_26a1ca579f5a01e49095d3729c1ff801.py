#Factores Primos
def  descomponer(n):
    facprimos=[]
    for i in range (2,n+1):
        while n % i ==0:
            facprimos.append(i)
            n=n/i
    return facprimos
n=int(input('porfavor ingrese un numero: '))
respuesta=descomponer(n)
for valor in respuesta:
    print(valor)
    