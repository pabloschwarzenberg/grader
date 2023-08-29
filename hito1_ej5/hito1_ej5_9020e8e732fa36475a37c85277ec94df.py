rut = input("Ingrese un número de RUT: ")

rut = rut[::-1]
suma = 0
factor = 2

for digito in rut:
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