# Solicitar al usuario que ingrese el número del RUT
rut = input("Ingrese el número del RUT (sin dígito verificador): ")

# Calcular el dígito verificador utilizando el algoritmo de Módulo 11
suma = 0
multiplicador = 2

for digito in reversed(rut):
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador == 8:
        multiplicador = 2

resto = suma % 11
dv = 11 - resto

# Manejar el caso especial del dígito verificador igual a 11
if dv == 10:
    dv = "K"
elif dv == 11:
    dv = 0

# Imprimir el resultado
print("dv =", dv)
