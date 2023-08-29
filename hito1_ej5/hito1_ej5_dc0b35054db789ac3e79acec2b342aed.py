#Cálculo del dígito verificador de un rut
rut = input("Ingrese un número de rut sin dígito verificador: ")

suma = 0
multiplo = 2

for i in reversed(rut):
    suma += int(i) * multiplo
    multiplo += 1
    if multiplo == 8:
        multiplo = 2

dv = 11 - (suma % 11)

if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

print("dv=" + str(dv))     