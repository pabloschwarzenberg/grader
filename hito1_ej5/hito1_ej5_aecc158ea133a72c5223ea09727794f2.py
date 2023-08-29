#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de RUT (sin el dígito verificador): ")

rut = rut[::-1]  # Invertir el RUT

suma = 0
multiplo = 2

for digito in rut:
    suma += int(digito) * multiplo
    multiplo += 1
    if multiplo == 8:
        multiplo = 2

resto = suma % 11
dv = 11 - resto

if dv == 10:
    dv = 'K'
elif dv == 11:
    dv = '0'

print("dv =", dv)
      