#Cálculo del dígito verificador de un rut
# Solicitar al usuario que ingrese el RUT sin dígito verificador
rut_sin_dv = input("Ingrese el RUT (sin dígito verificador): ")

# Calcular el dígito verificador
factor = 2
suma = 0

# Recorrer el RUT de derecha a izquierda
for i in range(len(rut_sin_dv) - 1, -1, -1):
    suma += int(rut_sin_dv[i]) * factor
    factor += 1
    if factor == 8:
        factor = 2

# Calcular el dígito verificador
digito_verificador = 11 - (suma % 11)

# Verificar si el dígito verificador es 11
if digito_verificador == 11:
    digito_verificador = 0

# Imprimir el resultado
print("dv =", digito_verificador)
      