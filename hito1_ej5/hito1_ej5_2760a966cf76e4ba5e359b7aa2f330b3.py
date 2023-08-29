#Cálculo del dígito verificador de un rut
rut = input("Ingrese su RUT: ")
c = len(rut)
a = 2
d = 0
while c>0:
    if a <= 7:
        b = int(rut[c-1])*a
        c -= 1
        a += 1
        d = d + b
    if a > 7:
        a = 2
c = d % 11
dv = 11 - c
if dv == 10:
    print("dv= k")
if dv == 11:
    print ("dv= 0")
else:
    print("dv=", str(dv))