#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de RUT sin dígito verificador: ")
factor = 2
suma = 0
for i in range(len(rut) - 1, -1, -1):
    suma += int(rut[i]) * factor
    factor += 1
    if factor > 7:
        factor = 2
digito_verificador = 11 - (suma % 11)
if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = "K"
print("dv =", digito_verificador)      