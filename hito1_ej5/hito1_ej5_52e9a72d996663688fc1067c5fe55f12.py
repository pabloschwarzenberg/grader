#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de RUT sin dígito verificador: ")

# Validar que el RUT sea un número entero positivo
if not rut.isdigit() or int(rut) <= 0:
    print("Error: El RUT debe ser un número entero positivo.")
    exit()

# Calcular el dígito verificador
rut = rut[::-1]  # Invertir el RUT
multiplicador = 2
suma = 0
for digito in rut:
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2
resto = suma % 11
dv = 11 - resto
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

print("dv =", dv)  