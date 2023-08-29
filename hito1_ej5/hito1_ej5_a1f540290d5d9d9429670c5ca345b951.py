# Solicitar el RUT al usuario
rut = input("Ingrese un número de RUT (sin dígito verificador): ")

# Calcular el dígito verificador
rut = rut[::-1]  # Invertir el RUT
multiplicador = 2
suma = 0

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

# Imprimir el dígito verificador
print("dv =", dv)
