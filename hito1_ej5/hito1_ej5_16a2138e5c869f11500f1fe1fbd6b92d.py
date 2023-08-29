#Cálculo del dígito verificador de un rut
rut = input("Ingrese un número de RUT (sin dígito verificador): ")

factor = 2
suma = 0

for i in reversed(rut):
    suma += int(i) * factor
    factor += 1
    if factor == 8:
        factor = 2

resto = suma % 11
digito_verificador = 11 - resto
if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = 'K'

print("dv =", digito_verificador)
     