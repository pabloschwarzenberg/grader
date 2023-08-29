# Usamos el rut ingresado por el usuario en reversa
rut = input("Rut: ")[::-1]

seq = [2, 3, 4, 5, 6, 7]

suma = 0
for i in range(len(rut)):
    suma += int(rut[i]) * seq[i % len(seq)]

dv = 11 - suma % 11

if dv == 11:
    print("dv=0")
elif dv == 10:
    print("dv=k")
else:
    print("dv=" + str(dv))
