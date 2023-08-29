rut = input("Ingrese un número de RUT (sin dígito verificador): ")

rut_reversed = rut[::-1]  # Invierte el orden del RUT
factor = 2
suma = 0

for d in rut_reversed:
    suma += int(d) * factor
    factor += 1
    if factor > 7:
        factor = 2

resto = suma % 11
dv = 11 - resto

if dv == 11:
    dv = '0'
elif dv == 10:
    dv = 'K'

print("dv =", dv)