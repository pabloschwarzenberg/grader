#Sistema de Ecuaciones
a = int(input("A:"))
b = int(input("B:"))
c = int(input("c:"))
d = int(input("D:"))
e = int(input("E:"))
f = int(input("F:"))

det = a*e - b*d

if det != 0:
     x = (c*e - b*f)/det
     y = (a*f - c*d)/det

print("x=",x)
print("y=",y)

      