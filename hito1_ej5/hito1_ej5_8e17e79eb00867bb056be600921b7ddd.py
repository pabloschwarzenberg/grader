rut = input("Ingrese el Rut sin dígito verificador: ")

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
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = 'K'

print("dv =", digito_verificador)
