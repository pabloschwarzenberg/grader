#Factores Primos
numero=int(input("ingrese numero:"))
a=2

while numero != 1:
    if numero%a==0:
        print(a)
        numero=numero/a
    else:
        a=a+1
	     