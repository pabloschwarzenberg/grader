#Factores Primos
## ENTRADA DE DATOS - PROCESO - SALIDA

Número = int(input("Ingrese un Número entero: "))

Factor_primo = 2
while Factor_primo <= Número:
    if Número % Factor_primo == 0:
        print(Factor_primo)
        Número = Número / Factor_primo
    else:
        Factor_primo = Factor_primo + 1   