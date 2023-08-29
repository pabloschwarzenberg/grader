#Sistema de Ecuaciones

m1=int(input("x1: "))
p1=int(input("y1: "))
l1=int(input("Solucion1: "))
m2=int(input("x2: "))
p2=int(input("y2: "))
l2=int(input("Solucion2: "))

z = m1*p2 - p1* m2
x=(l1*p2 - p1*l2)/z
y=(m1*l2 - l1*m2)/z

print("x=",x)
print("y=",y)