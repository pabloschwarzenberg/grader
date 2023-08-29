rut = input("Ingrese el número de RUT (sin dígito verificador): ")

# Calculando el dígito verificador
factor = 2
suma = 0

# Suma ponderada de los dígitos del RUT
for i in range(len(rut) - 1, -1, -1):
    suma += int(rut[i]) * factor
    factor += 1
    if factor == 8:
        factor = 2

# Calculando el dígito verificador
dv = 11 - (suma % 11)
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

print("dv=" + str(dv))