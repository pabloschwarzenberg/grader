# Pedimos al usuario que ingrese el número del RUT
rut = input("Ingresa tu RUT sin puntos ni guión: ")

# Calculamos el dígito verificador
factor = 2
suma = 0
for i in reversed(rut):
    suma += int(i) * factor
    factor += 1
    if factor == 8:
        factor = 2
digito_verificador = 11 - (suma % 11)
if digito_verificador == 11:
    digito_verificador = "0"
elif digito_verificador == 10:
    digito_verificador = "K"

# Imprimimos el resultado
print("dv=" + str(digito_verificador))