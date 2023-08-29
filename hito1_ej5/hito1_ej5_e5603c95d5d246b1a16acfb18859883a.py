#Cálculo del dígito verificador de un rut
# Solicitar al usuario que ingrese un número de RUT sin el dígito verificador
numero_rut = input("Ingrese un número de RUT (sin el dígito verificador): ")

# Inicializar variables
factor = 2
suma = 0

# Calcular la suma ponderada de los dígitos del RUT
for digito in reversed(numero_rut):
    suma += int(digito) * factor
    factor += 1
    if factor == 8:
        factor = 2

# Calcular el dígito verificador
resto = suma % 11
dv = 11 - resto
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

# Imprimir el dígito verificador
print("dv =", dv)
