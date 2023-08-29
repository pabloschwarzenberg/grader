#Sistema de Ecuaciones
print("Ingrese","ecuación","1",":","a","x","+","b","y","=","c")
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
print("Ingrese","ecuación","2",":","d","x","+","e","y","=","f")
d=float(input("d:"))
e=float(input("e:"))
f=float(input("f:"))
x=(c*e-b*f)/(a*e-b*d)
y=(c-a*x)/b
print("x=",x,"y=",y)
print("El valor de x es:",x )
print("El valor de y es:",y )
