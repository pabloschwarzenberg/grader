#Cálculo del dígito verificador de un rut
      # Obtener el número de RUT del usuario
rut = input("Ingrese el número de RUT (sin dígito verificador): ")

# Calcular el dígito verificador
factor = 2
suma = 0

for digito in reversed(rut):
    suma += int(digito) * factor
    factor += 1
    if factor > 7:
        factor = 2

dv = 11 - (suma % 11)

if dv == 11:
    dv = 0
elif dv == 10:
    dv = 'K'

# Imprimir el resultado
print("dv =", dv)
