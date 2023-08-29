#Cálculo del dígito verificador de un rut
 # Calcular el dígito verificador como el complemento a 11 del resto de la división por 11
rut = input("Ingresa el RUT sin dígito verificador: ")

# Convertir los caracteres del RUT a una lista de enteros
numeros = [int(d) for d in rut]

# Sumar los productos de cada dígito por su peso correspondiente
suma = 0
for i, digito in enumerate(numeros[::-1]):
    peso = (i % 6) + 2
    suma += peso * digito

# Calcular el dígito verificador como el complemento a 11 del resto de la división por 11
resto = suma % 11
dv = 11 - resto
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

print("dv =", dv)
