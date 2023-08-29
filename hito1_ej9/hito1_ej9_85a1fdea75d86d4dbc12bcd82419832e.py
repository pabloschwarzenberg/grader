#Sistema de Ecuaciones

a = float (input('ingrese quien acompaña a x en la 1era ecuación'))
b = float (input('ingrese quien acompaña a y en la 1era ecuación'))
c = float (input('ingrese igual a en la 1era ecuación'))
d = float (input('ingrese quien acompaña a x en la 2da ecuación'))
e = float (input('ingrese quien acompaña a y en la 2da ecuación'))
f = float (input('ingrese igual a en la 2da ecuación'))

det = a*e - b*d

if det != 0 :
    x = (e*c - b*f) / det
    y = (a*f - d*c) / det

print ("x=",  round(x,1))
print ("y=", round (y,1))

