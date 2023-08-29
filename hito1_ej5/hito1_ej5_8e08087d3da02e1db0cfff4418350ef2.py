#Cálculo del dígito verificador de un rut
# Pedir el número de RUT al usuario
rut = input("Ingrese el número de RUT (sin dígito verificador): ")

# Calcular el dígito verificador
suma = 0
multiplo = 2

# Recorrer el RUT en sentido inverso
for i in range(len(rut) - 1, -1, -1):
    suma += int(rut[i]) * multiplo
    multiplo += 1
    if multiplo == 8:
        multiplo = 2

# Calcular el dígito verificador como el complemento de la suma módulo 11
dv = 11 - (suma % 11)
if dv == 11:
    dv = 0
elif dv == 10:
    dv = 'K'

# Imprimir el dígito verificador
print("dv =", dv)
      