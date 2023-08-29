#Cálculo del dígito verificador de un rut
rut_incompleto = int( input("Ingrese datos: "))
a = str(rut_incompleto)

if (rut_incompleto//1000000)<10:
    b=int(a[:1])*2 + int(a[1:2])*7 + int(a[2:3])*6 + int(a[3:4])*5 + int(a[4:5])*4 + int(a[5:6])*3 + int(a[-1:])*2
else:
    b=int(a[:1])*3 + int(a[1:2])*2 + int(a[2:3])*7 + int(a[3:4])*6 + int(a[4:5])*5 + int(a[5:6])*4 + int(a[6:7])*3 + int(a[-1:])*2
c = b//11
d = b - 11*c
e = 11 - d
if e == 11:
    print("dv = 0")
elif e == 10:
    print("dv = k")
else :
    print("dv =", e)

