#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de RUT (sin dígito verificador): ")

# Revertir el RUT y convertirlo en una lista de dígitos
rut_revertido = list(reversed(rut))

# Variable para almacenar la suma acumulada
suma = 0

# Variable para el multiplicador
multiplicador = 2

# Calcular la suma ponderada de los dígitos
for digito in rut_revertido:
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

# Calcular el dígito verificador
resto = suma % 11
digito_verificador = 11 - resto

# Si el dígito verificador es 11, se reemplaza por 0
if digito_verificador == 11:
    digito_verificador = 0
# Si el dígito verificador es 10, se reemplaza por 'K'
elif digito_verificador == 10:
    digito_verificador = 'K'

print("dv =", digito_verificador)
