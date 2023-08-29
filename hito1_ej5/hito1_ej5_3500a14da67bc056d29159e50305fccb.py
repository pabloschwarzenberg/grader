#Cálculo del dígito verificador de un rut
# Solicitar al usuario ingresar el número de RUT
rut = input("Ingrese el número de RUT (sin dígito verificador): ")

rut_invertido = rut[::-1]

factor = 2
suma = 0

for digito in rut_invertido:
    suma += int(digito) * factor
    factor += 1
    if factor > 7:
        factor = 2

dv = 11 - (suma % 11)
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

print("dv =", dv)
