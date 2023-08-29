#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese un RUT sin dígito verificador: "))

suma = 0
multiplicador = 2
while rut > 0:
    suma += (rut % 10) * multiplicador
    rut = rut // 10
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

resto = suma % 11
dv = 11 - resto

if dv == 11:
    dv = "0"
elif dv == 10:
    dv = "K"
else:
    dv = str(dv)

print("dv={}".format(dv))
