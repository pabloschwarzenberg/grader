#Factores Primos
print("Numeros Primos")
numero=int(input("Ingrese Numero:"))
esPrimo=True
x=2
while x<numero-1:
    if numero % x ==0:
        print(x)
    x+=1
      