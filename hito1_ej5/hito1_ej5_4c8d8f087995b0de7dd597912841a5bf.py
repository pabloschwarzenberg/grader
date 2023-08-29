# Solicitar el número de RUT al usuario
rut = input("Ingrese el número de RUT (sin dígito verificador): ")

# Invertir el número de RUT
rut_invertido = rut[::-1]

# Calcular el dígito verificador
suma = 0
multiplicador = 2
for digito in rut_invertido:
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

resto = suma % 11
dv = 11 - resto
if dv == 10:
    dv = "K"
elif dv == 11:
    dv = 0

# Imprimir el resultado
print("dv =", dv)
