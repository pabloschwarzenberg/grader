rut = input("Ingrese el número de RUT (sin dígito verificador): ")

rut = rut[::-1]  # Invertir el orden del RUT

suma = 0
multiplicador = 2

for digito in rut:
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador == 8:
        multiplicador = 2

resto = suma % 11
dv = 11 - resto

if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

print("dv =", dv)
