#Cálculo del dígito verificador de un rut
# Solicitar al usuario ingresar el RUT sin dígito verificador
rut = input("Ingrese el RUT sin dígito verificador: ")

# Calcular el dígito verificador
factor = 2
suma = 0

# Iterar sobre los dígitos del RUT en orden inverso
for digito in reversed(rut):
    suma += int(digito) * factor
    factor += 1
    if factor > 7:
        factor = 2

# Calcular el dígito verificador como el complemento a 11 del resto de la suma
resto = suma % 11
dv = 11 - resto

# Manejar casos especiales para dígitos verificadores 10 y 11
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

# Imprimir el resultado
print("dv =", dv)
      