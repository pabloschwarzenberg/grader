
rut = input("Ingrese el RUT sin dígito verificador: ")

factor = 2
suma = 0

for i in reversed(rut):
    suma += int(i) * factor
    factor += 1
    if factor > 7:
        factor = 2

dv = 11 - (suma % 11)
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

print("dv =", dv)