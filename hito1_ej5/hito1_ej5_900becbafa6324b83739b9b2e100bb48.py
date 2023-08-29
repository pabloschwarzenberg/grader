#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de Rut (sin dígito verificador): ")

reversed_rut = rut[::-1]
multiplicando = 2
sumando = 0

for digito in reversed_rut:
    sumando += int(digito) * multiplicando
    multiplicando += 1
    if multiplicando > 7:
        multiplicando = 2


resto = sumando % 11
dv = 11 - resto
if dv == 10:
    dv = 'K'
elif dv == 11:
    dv = 0

print(f"dv = {dv}")
    