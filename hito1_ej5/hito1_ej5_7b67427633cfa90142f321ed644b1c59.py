#Cálculo del dígito verificador de un rut
a = int(input('ingrese su rut sin puntos: '))
b = str(a)
c = b[0]
d = b[1]
e = b[2]
f = b[3]
g = b[4]
h = b[5]
i = b[6]

cc = int(c)*3
dd = int(d)*2
ee = int(e)*7
ff = int(f)*6
gg = int(g)*5
hh = int(h)*4
ii = int(i)*3

suma = (cc+dd+ee+ff+gg+hh+ii)
div = (suma/11)
div1 = int(div)
sum2 = suma-(11*div1)
rest = 11-sum2
print('dv =',rest)
      