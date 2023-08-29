def ecuacion(a,b,c,d,e,f):
    y = (f*a-d*c)/(-d*b+e*a)
    x = (f*b-e*c)/(b*d-a*e)
    return print("x={}\ny={}".format(x,y))
a = float(input("ingrese primer valor:"))
b = float(input("ingrese primer valor:"))
c = float(input("ingrese primer valor:"))
d = float(input("ingrese primer valor:"))
e = float(input("ingrese primer valor:"))
f = float(input("ingrese primer valor:"))

ecuacion(a,b,c,d,e,f)
