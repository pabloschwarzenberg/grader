#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de RUT (sin el dígito verificador): ")

rut_reverso = rut[::-1]  # Revertir el RUT
multiplicador = 2
suma = 0

for digito in rut_reverso:
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

resto = suma % 11
digito_verificador = 11 - resto
if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = "K"

print("dv =", digito_verificador)
