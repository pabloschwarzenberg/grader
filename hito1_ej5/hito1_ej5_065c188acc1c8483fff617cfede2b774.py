rut = input("Ingrese su rut: ")
rut = rut.replace(".", "")
rut = rut.replace("-", "")

suma = 0
multiplicador = 2

for i in range(len(rut) - 1, -1, -1):
    suma += int(rut[i]) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

digito_verificador = 11 - (suma % 11)

if digito_verificador == 10:
    digito_verificador = "k"
elif digito_verificador == 11:
    digito_verificador = "0"

print("dv=" + str(digito_verificador))
