rut = input("Ingrese el número de RUT sin dígito verificador: ")

# Revertir el RUT para comenzar a multiplicar desde la posición más a la derecha
rut_revertido = rut[::-1]

# Variables para almacenar la suma y el multiplicador
suma = 0
multiplicador = 2

# Calcular la suma ponderada
for digito in rut_revertido:
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador == 8:
        multiplicador = 2

# Calcular el dígito verificador
resto = suma % 11
dv = 11 - resto
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

print("dv =", dv)

     