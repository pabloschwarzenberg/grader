rut = input("Ingrese rut: ")
rutlis = []
multiplicador = 2

for i in reversed(rut):
    rutlis.append(int(i)*multiplicador)
    multiplicador += 1
    if multiplicador == 8:
        multiplicador -= 6
suma = sum(rutlis)

dv = 11 - (suma % 11)
if dv == 11:
    print("DV=0")
elif dv == 10:
    print("DV=K")
else:
    print("DV=" + str(dv))