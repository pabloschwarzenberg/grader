#Sistema de Ecuaciones
a = float(input("a :"))
b = float(input("b :"))
c = float(input("c :"))
d = float(input("d :"))
e = float(input("e :"))
f = float(input("f :"))

x1a = (e*c)-(b*f)
x1b = (a*e)-(b*d)
x1 = x1a / x1b

y1a = (a*f)-(d*c)
y1b = (a*e)-(b*d)
y1 = y1a / y1b

print ("X=",x1)
print ("Y=",y1)
