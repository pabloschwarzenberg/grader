# Solicitar al usuario ingresar el número de RUT sin el dígito verificador
rut = input("Ingrese el número de RUT sin el dígito verificador: ")

# Inicializar variables
factor = 2
suma = 0

# Calcular la suma ponderada de los dígitos del RUT
for i in reversed(rut):
    suma += int(i) * factor
    factor += 1
    if factor > 7:
        factor = 2

# Calcular el dígito verificador
resto = suma % 11
dv = 11 - resto
if dv == 11:
    dv = 0
elif dv == 10:
    dv = 'K'

# Imprimir el resultado
print("dv =", dv)