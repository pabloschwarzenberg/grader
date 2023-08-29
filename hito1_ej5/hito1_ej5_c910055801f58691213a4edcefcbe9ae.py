#Cálculo del dígito verificador de un rut
rut = input(">>> ")
if len(rut) < 8:
    ceros = (8-len(rut))*"0"
    print(ceros)
    rut = ceros+rut
multiplicador = 2
i = -1
suma_de_los_productos = 0
while i >= -8:
    if multiplicador > 7:
        multiplicador = 2
    suma_de_los_productos += int(rut[i])*multiplicador
    multiplicador += 1
    i -= 1
dv = 11 - (suma_de_los_productos%11)
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "k"
print ("dv=",dv)