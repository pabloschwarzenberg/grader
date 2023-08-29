#Descomponer un número
# Entrada
num = str(input("Ingrese numero: "))

# Proceso
if len(num) == 1:
    uni = num[0]
    print(uni + "U")

if len(num) == 2:
    dec = num[0]
    uni = num[1]
    print(dec + "D", "+", uni + "U")


if len(num) == 3:
    cen = num[0]
    dec = num[1]
    uni = num[2]
    print(cen + "C", "+", dec + "D", "+", uni + "U")

if len(num) == 4:
    mil = num[0]
    cen = num[1]
    dec = num[2]
    uni = num[3]
    print(mil + "M", "+", cen + "C", "+", dec + "D", "+", uni + "U")