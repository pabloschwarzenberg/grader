rut = input("Ingrese su rut: ")
multiplicador = 2
i = len(rut) -1
suma_rut = 0

while i >= 0:
    suma_rut = suma_rut + (int(rut[i]) * multiplicador)
    multiplicador = multiplicador + 1
    if multiplicador == 8:
        multiplicador = 2
    i= i - 1

resto_rut = suma_rut % 11
digito_dv = 11- resto_rut

if digito_dv == 11:
    digito_dv = 0
elif digito_dv == 10:
    digito_dv = "k"

print("dv=", digito_dv)
     