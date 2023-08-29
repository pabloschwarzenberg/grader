rut = input("Ingrese el RUT sin dígito verificador (sin guiones): ")

# Calcular el dígito verificador
suma = 0
multiplicador = 2

for digito in reversed(rut):
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador == 8:
        multiplicador = 2

resto = suma % 11
digito_verificador = 11 - resto

# Convertir el dígito verificador a letra o número
if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = 'K'

print("dv =", digito_verificador)
