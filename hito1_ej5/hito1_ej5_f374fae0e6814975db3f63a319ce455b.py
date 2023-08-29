#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de RUT sin el dígito verificador: ")

reversed_rut = rut[::-1]
factor = 2
suma = 0

for digito in reversed_rut:
    suma += int(digito) * factor
    factor += 1
    if factor > 7:
        factor = 2

resto = suma % 11
dv = 11 - resto
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

print("dv =", dv)
      