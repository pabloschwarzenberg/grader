#Sistema de Ecuaciones
a1 = float(input("a1 = "))

b1 = float(input("b1 = "))

c1 = float(input("c1 = "))

a2 = float(input("a2 = "))

b2 = float(input("b2 = "))

c2 = float(input("c2 = "))

if a1/a2==b1/b2 and b1/b2==c1/c2:

  print("Infinitas soluciones")

elif a1/a2==b1/b2 and b1/b2!=c1/c2:

  print("No tiene solución")

else:

  x=(c1*b2-c2*b1)/(a1*b2-a2*b1)

  y=(a1*c2-a2*c1)/(a1*b2-a2*b1)

  print("x=", round(x,1))

  print("y=", round(y,1))      