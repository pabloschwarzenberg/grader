#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de RUT (sin el dígito verificador): ")

# Cálculo del dígito verificador
reversed_rut = reversed(rut)
multiplicador = 2
suma = 0

for digito in reversed_rut:
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador == 8:
        multiplicador = 2

resto = suma % 11
dv = 11 - resto
if dv == 10:
    dv = "K"
elif dv == 11:
    dv = 0

# Imprimir el resultado
print("dv =", dv)
