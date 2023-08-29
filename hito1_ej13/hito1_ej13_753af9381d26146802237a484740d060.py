#Factores Primos
x = int(2)
NPrimo = int(input("Ingrese el numero: "))
while(NPrimo != 1):
    if (NPrimo % x == 0 ):
        print(str(x) + "")
        NPrimo = NPrimo / x
    else:
        x = x + 1   