# Solicitar al usuario que ingrese el número del RUT sin dígito verificador
rut = input("Ingrese el número del RUT sin dígito verificador: ")

# Calcular el dígito verificador
rut = rut[::-1]  # Invertir el RUT para facilitar el cálculo
factor = 2
suma = 0

for digito in rut:
    suma += int(digito) * factor
    factor += 1
    if factor == 8:
        factor = 2

dv = 11 - (suma % 11)

if dv == 10:
    dv = "K"
elif dv == 11:
    dv = 0

# Imprimir el resultado
print("dv =", dv)
      