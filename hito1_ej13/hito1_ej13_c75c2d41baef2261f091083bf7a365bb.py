#Factores Primos
x=int(input('Ingrese numero: '))
i=2
while i<x:
    p1=x%i
    if p1==0:
        print(i)
    i=i+1
