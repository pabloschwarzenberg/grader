# Cálculo del dígito verificador de un rut
# Obtener el RUT del usuario
rut = input("Ingrese un número de RUT (sin dígito verificador): ")

# Calcular el dígito verificador
suma = 0
multiplicador = 2

for digito in reversed(rut):
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

resto = suma % 11
digito_verificador = 11 - resto

if digito_verificador == 11:
    digito_verificador = "0"
elif digito_verificador == 10:
    digito_verificador = "K"

# Imprimir el resultado
print("dv =", digito_verificador)
