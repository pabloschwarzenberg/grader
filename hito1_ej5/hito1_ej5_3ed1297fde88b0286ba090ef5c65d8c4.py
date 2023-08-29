rut = input()

rut_reversado = list(rut[::-1])

suma = 0
multiplicador = 2
for digito in rut_reversado:
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

resto = suma % 11
dv = 11 - resto

if dv == 10:
    dv = 'k'
elif dv == 11:
    dv = 0

print("dv=" + str(dv))

      