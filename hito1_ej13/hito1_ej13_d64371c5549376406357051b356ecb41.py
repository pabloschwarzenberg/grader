#Factores Primos
n=2
numero=int(input('ingrese un numero: '))
while numero!=1:
    if numero%n==0:
        print(n)
        numero=numero/n
    else:
        n+=1
