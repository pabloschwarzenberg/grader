rut = input("Ingrese el número de RUT sin dígito verificador: ")
suma = 0
multiplo = 2
for digito in reversed(rut):
    suma += int(digito) * multiplo
    multiplo += 1
    if multiplo == 8:
        multiplo = 2
resto = suma % 11
digito_verificador = 11 - resto
if digito_verificador == 11:
    digito_verificador = "0"
elif digito_verificador == 10:
    digito_verificador = "k"
print("dv =", digito_verificador)
