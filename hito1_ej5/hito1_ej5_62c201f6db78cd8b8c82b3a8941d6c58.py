rut = input("Ingresa el número de RUT: ")

rut = rut[::-1]  # Invertir el RUT

multiplicador = 2
suma = 0

for digito in rut:
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador == 8:
        multiplicador = 2

verificador = 11 - (suma % 11)
if verificador == 11:
    verificador = "0"
elif verificador == 10:
    verificador = "K"
else:
    verificador = str(verificador)

print("dv =", verificador)
