rut = input("Ingrese el número de RUT (sin el dígito verificador): ")

suma = 0
factor = 2
for digito in reversed(rut):
    suma += int(digito) * factor
    factor += 1
    if factor == 8:
        factor = 2

resto = suma % 11
digito_verificador = 11 - resto

if digito_verificador == 11:
    dv = "0"
elif digito_verificador == 10:
    dv = "K"
else:
    dv = str(digito_verificador)

if dv == "K":
    dv = "k"

print("dv =", dv)