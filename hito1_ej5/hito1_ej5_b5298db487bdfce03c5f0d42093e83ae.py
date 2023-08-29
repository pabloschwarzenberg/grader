#Cálculo del dígito verificador de un rut
rut = str(input("Por Favor ingrese el numero: "))
a = int(rut[0])
b = int(rut[1])
c = int(rut[2])
d = int(rut[3])
e = int(rut[4])
f = int(rut[5])
g = int(rut[6])
#h = int(rut[7])

a1 = a * 3
b1 = b * 2
c1 = c * 7
d1 = d * 6
e1 = e * 5
f1 = f * 4
g1 = g * 3
h1 = h * 2
suma = a1 + b1 + c1 + d1 + e1 + f1 + g1 + h1
suma1 = suma//11
suma2 = suma - (11* suma1)
suma3 = 11 - suma2
if suma3 == 11:
    print("dv= 0")
if suma3 == 10:
    print("dv=K")
else:
    print("dv=",suma3)     