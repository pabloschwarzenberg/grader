
# Solicitar el RUT al usuario
rut = input("Ingrese el RUT sin dígito verificador: ")

# Calcular el dígito verificador
suma = 0
multiplo = 2

# Iterar sobre los dígitos del RUT en orden inverso
for i in reversed(rut):
    suma += int(i) * multiplo
    multiplo = multiplo + 1 if multiplo < 7 else 2

resto = suma % 11
dv = 11 - resto if resto != 0 else 0

# Imprimir el resultado
print("dv =", dv)