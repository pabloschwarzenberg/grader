rut = input("Ingrese un número de RUT: ")
rut = rut.replace(".", "")
rut = rut.replace("-", "")

factor = 2
suma = 0

for i in range(len(rut)-1, -1, -1):
    suma += int(rut[i]) * factor
    factor += 1
    if factor == 8:
        factor = 2

dv = 11 - (suma % 11)

if dv == 11:
    dv = "0"
elif dv == 10:
    dv = "K"

print("dv=" + str(dv))