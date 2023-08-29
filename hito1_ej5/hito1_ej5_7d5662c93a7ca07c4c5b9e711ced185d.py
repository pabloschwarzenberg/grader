#Cálculo del dígito verificador de un rut
# Pedir al usuario el número del Rut
rut = input("Ingrese el número del Rut sin dígito verificador: ")

# Variables para almacenar la suma y el multiplicador
suma = 0
multiplicador = 2

# Calcular la suma ponderada
for i in range(len(rut)-1, -1, -1):
    suma += int(rut[i]) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

# Calcular el dígito verificador
digito_verificador = 11 - (suma % 11)
if digito_verificador == 11:
    dv = "0"
elif digito_verificador == 10:
    dv = "K"
else:
    dv = str(digito_verificador)

# Imprimir el resultado
print("dv =", dv)
