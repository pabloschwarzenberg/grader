#Factores Primos
x=int(2)
numero=int(input("Ingrese su numero:"))

while (numero !=1):
    if (numero % x== 0):
        print(str(x) + " ")
        numero=numero/x
    else:
        x=x+1
     