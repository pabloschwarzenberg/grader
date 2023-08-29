#Cálculo del dígito verificador de un rut
rut = input("Ingresa el RUT sin dígito verificador: ")

# Calcula el dígito verificador
suma = 0
multiplo = 2
for i in reversed(rut):
    suma += int(i) * multiplo
    multiplo += 1
    if multiplo == 8:
        multiplo = 2

resto = suma % 11
dv = 11 - resto
if dv == 10:
    dv = 'K'
elif dv == 11:
    dv = 0

print("dv =", dv)      