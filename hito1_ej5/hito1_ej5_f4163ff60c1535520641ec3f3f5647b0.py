#Cálculo del dígito verificador de un rut
rut = input("Ingrese el RUT (sin el dígito verificador): ")

# Verificar que el RUT sea válido
if not rut.isdigit() or len(rut) < 1:
    print("El RUT ingresado no es válido.")
    exit()

# Convertir el RUT a una lista de dígitos
rut_digits = list(map(int, rut[::-1]))

# Calcular el dígito verificador
multiplier = 2
total = 0
for digit in rut_digits:
    total += digit * multiplier
    multiplier = multiplier + 1 if multiplier < 7 else 2

verificador = 11 - (total % 11)

# Si el dígito verificador es 11, se reemplaza por 0
if verificador == 11:
  dv = 0
elif verificador == 10:
  dv = "k"
else:
  dv = verificador

print("dv =", dv)