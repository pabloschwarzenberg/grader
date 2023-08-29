#Factores Primos
numero=int(input("Ingresar numero: "))
a=2
while a<=numero:
    if numero%a==0:
        print(a)
        numero=numero/a
    else:
            a+=1   