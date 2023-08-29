rut = input("Ingrese el número de RUT sin dígito verificador: ")

reversed_rut = rut[::-1]  # Invertir el RUT
factor = 2
suma = 0

for digito in reversed_rut:
    suma += int(digito) * factor
    factor += 1
    if factor == 8:
        factor = 2

resto = suma % 11
dv = 11 - resto
if dv == 10:
    dv = 'K'
elif dv == 11:
    dv = 0

print("dv =", dv)
