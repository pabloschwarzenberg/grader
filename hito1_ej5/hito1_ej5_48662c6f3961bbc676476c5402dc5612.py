#Cálculo del dígito verificador de un rut
rut = input("RUT: ")
n = 2
suma = 0
for i in range(len(rut)):
    suma += int(rut[len(rut) - 1 - i]) * n
    
    n += 1

    if n == 8:
        n = 2

dv = 11 - (suma % 11)

if dv == 11:
    dv = "0"

elif dv == 10:
    dv = "K"

print("dv={}".format(dv))