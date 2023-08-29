#Cálculo del dígito verificador de un rut
# Solicitar el número de rut al usuario
rut = input("Ingrese el número de rut (sin dígito verificador): ")

# Calcular el dígito verificador
rut = rut[::-1]  # Invertir el número de rut
factor = 2
suma = 0

for digito in rut:
    suma += int(digito) * factor
    factor += 1

resto = suma % 11
dv = 11 - resto

if dv == 11:
    dv = "0"
elif dv == 10:
    dv = "K"
else:
    dv = str(dv)

# Mostrar el resultado
print("dv =", dv)
      