rut = input("Ingresa un RUT sin dígito verificador: ")
rut = rut[::-1]
suma = 0
serie = [2, 3, 4, 5, 6, 7]
for i in range(len(rut)):
    suma += int(rut[i]) * serie[i % len(serie)]
resto = suma % 11
dv = 11 - resto
if dv == 11:
    dv = "0"
elif dv == 10:
    dv = "K"
else:
    dv = str(dv)
print("dv=" + dv)
