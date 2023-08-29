#Sistema de Ecuaciones
#Incio
a = float(input("Asigne un valor para a: "))
b = float(input("Asigne un valor para b: "))
c = float(input("Asigne un valor para c: "))
d = float(input("Asigne un valor para d: "))
e = float(input("Asigne un valor para e: "))
f = float(input("Asigne un valor para f: "))
#Procedimiento
x = (c*e - b*f)/(a*e - b*d)
y = (a*f - c*d)/(a*e - b*d)
c = a*x + b*y
f = d*x + e*y
print("x= ",round(x,1))
print("y= ",round(y,1))