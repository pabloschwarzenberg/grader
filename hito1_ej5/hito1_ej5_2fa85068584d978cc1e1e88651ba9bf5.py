#Cálculo del dígito verificador de un rut
# Obtener el Rut desde el usuario
rut = input("Ingrese el Rut (sin dígito verificador): ")

# Calcular el dígito verificador
suma = 0
multiplicador = 2

for digito in reversed(rut):
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

digito_verificador = 11 - (suma % 11)
if digito_verificador == 11:
    dv = "0"
elif digito_verificador == 10:
    dv = "K"
else:
    dv = str(digito_verificador)

# Imprimir el dígito verificador
print("dv=" + dv)