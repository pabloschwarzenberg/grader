#Cálculo del dígito verificador de un rut
 rut = input("Ingrese un número de Rut: ")

suma = 0
multiplicador = 2

for digito in reversed(rut):
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

dv = 11 - (suma % 11)
if dv == 11:
    dv = 0
elif dv == 10:
    dv = 'K'

print("dv =", dv)     