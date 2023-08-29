a1 = float(input("Introduce el coeficiente a1: "))
b1 = float(input("Introduce el coeficiente b1: "))
c1 = float(input("Introduce el término independiente c1: "))
a2 = float(input("Introduce el coeficiente a2: "))
b2 = float(input("Introduce el coeficiente b2: "))
c2 = float(input("Introduce el término independiente c2: "))

# Método de eliminación de Gauss
x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)

print("x={}".format(round(x, 1)))
print("y={}".format(round(y, 1)))

