#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de rut (sin dígito verificador): ")

# Revertir el número de rut
rut_revertido = rut[::-1]

# Calcular el dígito verificador
factor = 2
suma = 0

for d in rut_revertido:
    suma += int(d) * factor
    factor += 1
    if factor == 8:
        factor = 2

dv = 11 - (suma % 11)
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

print("dv =", dv)
      