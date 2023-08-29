#Cálculo del dígito verificador de un rut
# Solicitar al usuario el número de Rut
numero_rut = input("Ingrese un número de Rut: ")

# Invertir el número de Rut
numero_rut_invertido = numero_rut[::-1]

# Calcular el dígito verificador
suma = 0
multiplo = 2
for digito in numero_rut_invertido:
    suma += int(digito) * multiplo
    multiplo = multiplo + 1 if multiplo < 7 else 2

digito_verificador = 11 - (suma % 11)
if digito_verificador == 11:
    digito_verificador = "0"
elif digito_verificador == 10:
    digito_verificador = "K"

# Imprimir el resultado
print("dv =", digito_verificador)