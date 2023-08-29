a = float(input("Ingresa el coeficiente de x en la primera ecuación: "))
b = float(input("Ingresa el coeficiente de y en la primera ecuación: "))
c = float(input("Ingresa el término independiente de la primera ecuación: "))
d = float(input("Ingresa el coeficiente de x en la segunda ecuación: "))
e = float(input("Ingresa el coeficiente de y en la segunda ecuación: "))
f = float(input("Ingresa el término independiente de la segunda ecuación: "))

a1 = a * -e
b1 = b * -e
c1 = c * -e
d1 = d * b
e1 = e * b
f1 = f * b

x = (c1 + f1) / (a1 + d1)

a2 = a * -d
b2 = b * -d
c2 = c * -d
d2 = d * a
e2 = e * a
f2 = f * a

y = (c2 + f2) / (b2 + e2)

print("x=",x)
print("y=",y)
      