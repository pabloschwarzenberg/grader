#Sistema de Ecuaciones
a=float(input ())
b=float(input ())
c=float(input ())
d=float(input ())
e=float(input ())
f=float(input ())
g=(a*e-b*d)
if g == 0:
    print ("El sistema lamentablemente no tiene solucion")
else:
    x= (e*c-b*f)/(a*e-b*d)
    y= (a*f-d*c)/(a*e-b*d)
    print(round(x, 1),"x=",(x))  
    print(round(y, 1),"y=",(y))
  