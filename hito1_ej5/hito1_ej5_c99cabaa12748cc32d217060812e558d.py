#Cálculo del dígito verificador de un rut
numero_ingresado = int(input("Ingrese un RUT: "))
Multiplicador = 2
indice = 0
DV=0

while indice < len(str(numero_ingresado)):
    Largo = len(str(numero_ingresado))-1-indice
    DV = DV + int(str(numero_ingresado)[Largo]) * Multiplicador
    indice += 1
    Multiplicador += 1
    if Multiplicador > 7:
        Multiplicador = 2

CalculoDV = (int(DV)/11)*11
DV = 11 - (DV - CalculoDV)

if DV < 10:
    print("dv=" + str(DV))
if DV == 10:
    print("dv=k")
if DV == 11:
    print("dv=0")