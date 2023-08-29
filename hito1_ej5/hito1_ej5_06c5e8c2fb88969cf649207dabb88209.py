#Cálculo del dígito verificador de un rut
# Solicitar al usuario ingresar el número de rut
numero_rut = input("Ingrese el número de rut (sin dígito verificador): ")

# Calcular el dígito verificador
reversed_rut = reversed(numero_rut)  # Invertir el número de rut
factor = 2
suma = 0

for digito in reversed_rut:
    suma += int(digito) * factor
    factor += 1
    if factor > 7:
        factor = 2

resto = suma % 11
digito_verificador = 11 - resto

# Manejo de casos especiales
if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = "K"

# Imprimir el resultado
print("dv =", digito_verificador)      