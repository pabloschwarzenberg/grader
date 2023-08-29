#Cálculo del dígito verificador de un rut
rut = input("Ingrese el Rut (sin dígito verificador): ")

# Calcular el dígito verificador
rut = rut[::-1]  # Invertir el Rut
factor = 2
suma = 0

for digito in rut:
    suma += int(digito) * factor
    factor += 1
    if factor > 7:
        factor = 2

digito_verificador = 11 - (suma % 11)
if digito_verificador == 10:
    digito_verificador = "K"
elif digito_verificador == 11:
    digito_verificador = 0

# Imprimir el resultado
print("dv =", digito_verificador)      