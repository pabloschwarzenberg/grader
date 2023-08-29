#Cálculo del dígito verificador de un rut
RUT = int(input("Ingrese el numero de su RUT (sin considerar lo que viene posterior al guion): "))

a = RUT % 10000000
A = (a / 1000000)
b = RUT % 1000000
B = (b / 100000)
c = RUT % 100000
C = (c / 10000)
d = RUT % 10000
D = (d / 1000)
e = RUT % 1000
E = (e / 100)
f = RUT % 100
F = (f / 10)
g = (RUT % 10)

suma = (int(RUT // 10000000) * 3) + int(A) * 2 + int(B) * 7 + int(C) * 6 + int(D) * 5 + int(E) * 4 + int(F) * 3 + int(g) * 2
Parte_entera = suma // 11
Resto = suma % 11
dv = 11 - Resto
if(dv == 11):
    print("dv=0")
elif(dv == 10):
    print("dv=", "k")
elif((dv != 11) and (dv != 10)):
    print("dv=", dv)


