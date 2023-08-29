# Cálculo del dígito verificador de un RUT

# Solicitar el RUT al usuario
rut = input("Ingrese el RUT sin el dígito verificador (sin puntos ni guion): ")

# Calcular el dígito verificador
serie = [2, 3, 4, 5, 6, 7]
indice_serie = 0
suma = 0

for digito in reversed(rut):
    suma += int(digito) * serie[indice_serie]
    indice_serie = (indice_serie + 1) % 6

resto = suma % 11
digito_verificador = 11 - resto

if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = "K"

# Imprimir el resultado
print("dv =", digito_verificador)
