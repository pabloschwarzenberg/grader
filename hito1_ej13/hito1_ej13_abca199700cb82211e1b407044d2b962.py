#Factores Primos
numero = int(input("Ingrese su número: "))
t=2
while t<=numero:
    if numero%t==0:
        print(t)
        numero = numero/t
    else:
        t+=1      