#Cálculo del dígito verificador de un rut
      # Solicitar al usuario el número del RUT
rut = input("Ingrese el número de RUT (sin dígito verificador): ")

# Inicializar variables
factor = 2
suma = 0

# Calcular la suma ponderada
for digito in reversed(rut):
    suma += int(digito) * factor
    factor += 1
    if factor == 8:
        factor = 2

# Calcular el dígito verificador
dv = 11 - (suma % 11)
if dv == 10:
    dv = "K"
elif dv == 11:
    dv = 0

# Imprimir el resultado
print("dv =", dv)
