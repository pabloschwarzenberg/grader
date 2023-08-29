numero_rut = input("Ingrese el número del RUT (sin dígito verificador): ")
suma = 0
multiplicador = 2

for i in range(len(numero_rut)-1, -1, -1):
    suma += int(numero_rut[i]) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

resto = suma % 11
dv = 11 - resto

if dv == 10:
    dv = 'K'
elif dv == 11:
    dv = 0

print("dv =", dv)
