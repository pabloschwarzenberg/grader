rut = input("Ingrese un número de Rut (sin dígito verificador): ")

# Revertir el Rut
rut_revertido = rut[::-1]

# Calcular el dígito verificador
factor = 2
suma = 0
for digito in rut_revertido:
    suma += int(digito) * factor
    factor += 1

resto = suma % 11
digito_verificador = 11 - resto
if digito_verificador == 10:
    digito_verificador = "k"
else:
    digito_verificador = str(digito_verificador)

print("dv =", digito_verificador)

if digito_verificador == 11:
    digito_verificador = 0

print("dv =", digito_verificador)
