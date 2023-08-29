#Cálculo del dígito verificador de un rut
rut = input("Ingrese el RUT (sin dígito verificador): ")
factor = 2
suma = 0
for i in reversed(range(len(rut))):
    suma += int(rut[i]) * factor
    factor += 1
    if factor == 8:
        factor = 2
digito_verificador = 11 - (suma % 11)
if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = "K"
print("dv =", digito_verificador)     