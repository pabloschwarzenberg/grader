rut = input("Ingrese el número de RUT: ")
rut = rut.replace(".", "")  # Eliminar los puntos del RUT

suma = 0
multiplicador = 2

for i in range(len(rut) - 1, -1, -1):
    suma += int(rut[i]) * multiplicador
    multiplicador += 1
    if multiplicador == 8:
        multiplicador = 2

resto = suma % 11
dv = 11 - resto

if dv == 11:
    dv = "0"
elif dv == 10:
    dv = "K"
else:
    dv = str(dv)

print("dv=" + dv)