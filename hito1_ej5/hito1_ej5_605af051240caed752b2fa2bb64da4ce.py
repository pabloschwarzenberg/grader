#Cálculo del dígito verificador de un rut
rut = input("Ingrese un número de Rut sin el dígito verificador: ")

rut = rut[::-1]  # Invertir el Rut
multiplicador = 2
suma = 0

for digito in rut:
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

digito_verificador = 11 - (suma % 11)

if digito_verificador == 11:
    digito_verificador = "0"
elif digito_verificador == 10:
    digito_verificador = "K"

print("dv =", digito_verificador)
if digito_verificador == 11:
    digito_verificador = "0"
elif digito_verificador == 10:
    digito_verificador = "K"

print("El dígito verificador es:", digito_verificador)