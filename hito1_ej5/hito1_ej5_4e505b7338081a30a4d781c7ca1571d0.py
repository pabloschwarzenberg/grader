#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número del Rut sin dígito verificador: ")

suma = 0
multiplicador = 2

for i in range(len(rut)-1, -1, -1):
    suma += int(rut[i]) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

digito_verificador = 11 - (suma % 11)
if digito_verificador == 11:
    dv = "0"
elif digito_verificador == 10:
    dv = "K"
else:
    dv = str(digito_verificador)

print("dv =", dv)
      