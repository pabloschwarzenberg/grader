#Cálculo del dígito verificador de un rut
rut = input("Ingrese el Rut sin dígito verificador (sin puntos ni guiones): ")

# Revertir el Rut para empezar desde la unidad
rut_revertido = rut[::-1]

# Calcular el dígito verificador
suma = 0
multiplicador = 2
for digito in rut_revertido:
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador == 8:
        multiplicador = 2

resto = suma % 11
digito_verificador = 11 - resto
if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = "K"

# Imprimir el resultado
rut_completo = rut + str(digito_verificador)
print("El Rut completo con dígito verificador es:", rut_completo)
print( "DV = ",digito_verificador)  