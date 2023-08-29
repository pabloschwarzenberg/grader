#Cálculo del dígito verificador de un rut
# Obtener el número del RUT del usuario
rut = input("Ingrese el número del RUT (sin dígito verificador): ")

# Calcular el dígito verificador
reversed_rut = rut[::-1]  # Invertir el orden del RUT
factor = 2
suma = 0

for digito in reversed_rut:
    suma += int(digito) * factor
    factor += 1
    if factor == 8:
        factor = 2

resto = suma % 11
dv = 11 - resto
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

# Imprimir el resultado
print("dv =", dv)