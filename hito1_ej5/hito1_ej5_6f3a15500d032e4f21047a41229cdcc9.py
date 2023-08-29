#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de rut (sin dígito verificador): ")

# Revertir el número de rut
reversed_rut = rut[::-1]

# Calcular el dígito verificador
suma = 0
multiplo = 2
for digito in reversed_rut:
    suma += int(digito) * multiplo
    multiplo += 1
    if multiplo > 7:
        multiplo = 2

resto = suma % 11
dv = 11 - resto

# Imprimir el resultado
print("dv =", dv)
      