#Cálculo del dígito verificador de un rut
rut = input("Ingresa el número de RUT (sin dígito verificador): ")

# Calcula el dígito verificador
suma = 0
multiplicador = 2

# Itera sobre los dígitos del RUT en orden inverso
for digito in reversed(rut):
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

# Calcula el resto de la división
resto = suma % 11

# Calcula el dígito verificador
if resto == 1:
    dv = "K"
elif resto == 0:
    dv = "0"
else:
    dv = str(11 - resto)

rut_con_dv = rut + "-" + dv

print("RUT con dígito verificador:", rut_con_dv)

     