#Cálculo del dígito verificador de un rut
digito_verificador=0

#Cálculo del dígito verificador de un rut
rut = input("Ingrese su RUT sin puntos ni guión: ")
rut = rut[::-1]
multiplicador = 2
suma = 0
for i in rut:
    suma += int(i) * multiplicador
    multiplicador += 1
    if multiplicador == 8:
        multiplicador = 2
digito_verificador = 11 - (suma % 11)
if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = "K"
print("dv=" + str(digito_verificador))      