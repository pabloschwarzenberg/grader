#Sistema de Ecuaciones

a1 = int(input("a: "))
b1 = int(input("b: "))
c1 = int(input("c: "))

a2 = int(input("a: "))
b2 = int(input("b: "))
c2 = int(input("c: "))

x = ((c2*b1)-(b2*c1))/((a2*b1)-(a1*b2))
y = (c1 - (a1*x))/b1

print("x=",round(x,1))
print("y=",round(y,1))
