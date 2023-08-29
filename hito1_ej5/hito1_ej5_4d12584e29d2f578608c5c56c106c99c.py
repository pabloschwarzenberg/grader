# Obtener el Rut como dato
rut = input("Ingrese un número que represente el Rut: ")

# Calcular el dígito verificador
suma = 0
multiplicador = 2

for digito in reversed(rut):
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

# Imprimir el resultado
print("dv =", dv)

      