#Cálculo del dígito verificador de un rut
# Solicitar al usuario el número de RUT
numero_rut = input("Ingrese el número de RUT (sin dígito verificador): ")

# Calcular el dígito verificador
factor = 2
suma = 0

# Iterar sobre los dígitos del RUT en orden inverso
for digito in reversed(numero_rut):
    suma += int(digito) * factor
    factor += 1
    if factor > 7:
        factor = 2

# Calcular el dígito verificador como el complemento a 11 del resto de la suma
resto = suma % 11
digito_verificador = 11 - resto

# Manejar casos especiales: 10 -> "K", 11 -> "0"
if digito_verificador == 10:
    digito_verificador = "K"
elif digito_verificador == 11:
    digito_verificador = "0"

# Imprimir el resultado
print("dv =", digito_verificador)
      