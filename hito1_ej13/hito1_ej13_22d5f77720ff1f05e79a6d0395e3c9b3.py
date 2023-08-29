#Factores Primos
x = int(2)
numero_primo = int(input("Ingrese el numero:_ "))
while (numero_primo != 1):
    if (numero_primo % x == 0):
        print(str(x) + "")
        numero_primo = numero_primo / x
    else:
        x = x + 1      