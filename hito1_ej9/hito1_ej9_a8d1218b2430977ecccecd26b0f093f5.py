#Sistema de Ecuaciones
#2x+3y=6 y x+2y=5
#a1+b1=c1 y a2+b2=c2
a1 = 2
b1 = 3
c1 = 6
a2 = 1
b2 = 2
c2 = 5
producto = a1 * b2 - a2 * b1
x = (c1 * b2 - c2 * b1) / producto
y = (a1 * c2 - a2 * c1) / producto


print(f"X = {round(x,1)}")
print(f"Y = {round(y,1)}")

  