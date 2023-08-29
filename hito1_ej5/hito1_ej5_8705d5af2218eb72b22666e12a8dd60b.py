rut = input("Ingrese el número de Rut (sin el dígito verificador): ")

suma = 0
multiplo = 2

for digito in reversed(rut):
    suma += int(digito) * multiplo
    multiplo += 1
    if multiplo == 8:
        multiplo = 2

resto = suma % 11
dv = 11 - resto
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

print("dv =", dv)