print("Calcular el numero verificador.")
rut = int(input("Ingrese el rut sin puntos ni digito verificador: "))
a = (rut//10000000)
b = (rut//1000000) % 10
c = (rut//100000) % 10
d = (rut//10000) % 10
e = (rut//1000) % 10
f = (rut//100) % 10
g = (rut//10) % 10
h = (rut//1) % 10
ax = h*2
bx = g*3
cx = f*4
dx = e*5
ex = d*6
fx = c*7
gx = b*2
hx = a*3
suma = (ax+bx+cx+dx+ex+fx+gx+hx)
modulo = suma % 11
numeroverif = 11 - modulo


if numeroverif == 11:
    print("dv = 0")
else:
    if numeroverif == 10:
        print("dv = K")
    else:
        print("dv = ", numeroverif)    