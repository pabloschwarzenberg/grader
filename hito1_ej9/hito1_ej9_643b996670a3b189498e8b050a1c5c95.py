#Sistema de Ecuaciones
a=input()
b=input()
c=input()
d=input()
e=input()
f=input()
a = float(a)
b = float(b)
c = float(c)
d = float(d)
e = float(e)
f = float(f)

det = a * e - b * d

if det != 0 :
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det

    print ("x=",x)
    print ("y=",y)
