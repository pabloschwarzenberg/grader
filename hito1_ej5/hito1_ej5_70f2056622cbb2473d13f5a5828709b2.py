#Cálculo del dígito verificador de un rut
rut = input("Ingrese su rut: ")
rut2 = rut[::-1]
x = 0
cont = 2

for i in range(len(rut2)):
    x += int(rut2[i]) * cont
    cont += 1
    if cont > 7:
        cont = 2

y = x // 11
x = x - (y * 11)
dv = 11 - x

if dv == 11:
    print("dv = 0")
elif dv == 10:
    print("dv = K")
else:
    print("dv =", dv)