#Factores Primos
x= int(2)
numero= int(input("Ingresar el numero a calcular factor primo:"))

while (numero!=1):
    if (numero % x==0):
        print(str(x)+" ")
        numero = numero/x
    else:
        x = x+1
      