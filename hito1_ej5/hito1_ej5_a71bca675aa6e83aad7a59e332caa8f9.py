rut = input("Ingrese el número de rut sin dígito verificador: ")

rut_revertido = rut[::-1]

suma = 0
factor = 2
for digito in rut_revertido:
    suma += int(digito) * factor
    factor += 1
    if factor > 7:
        factor = 2

dv = 11 - (suma % 11)

if dv == 11:
    dv = 0

print("dv =", dv)
