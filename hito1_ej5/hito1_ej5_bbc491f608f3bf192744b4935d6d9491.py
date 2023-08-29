#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de RUT: ")
rut = str(rut)
rut = rut.replace(".", "")
rut = rut.replace("-", "")

multiplicador = 2
suma = 0

for i in range(len(rut)-1, -1, -1):
    digito = int(rut[i])
    suma += digito * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

resto = suma % 11
digito_verificador = 11 - resto

if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = "K"

print("dv=" + str(digito_verificador))