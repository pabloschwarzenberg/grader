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
dv = 11 - (suma % 11)
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"
print("dv=" + str(dv))
      