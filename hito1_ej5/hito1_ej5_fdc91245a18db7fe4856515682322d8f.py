#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de RUT (sin dígito verificador): ")

rut_reverso = rut[::-1]
serie_numerica = [2, 3, 4, 5, 6, 7]
suma = 0

for i in range(len(rut_reverso)):
    suma += int(rut_reverso[i]) * serie_numerica[i % len(serie_numerica)]

resto = suma % 11
digito_verificador = 11 - resto

if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = "K"

print("dv =", digito_verificador)