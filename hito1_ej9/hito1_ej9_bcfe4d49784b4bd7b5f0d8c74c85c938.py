a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el término independiente de la primera ecuación: "))
a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el término independiente de la segunda ecuación: "))

# Calculamos la solución del sistema mediante el método de sustitución
x = (c1 - b1*(c2/b2)) / (a1 - (b1*a2/b2))
y = (c2/b2) - (a2/b2)*x

print("x=",round(x,1),sep="")
print("y=",round(y,1),sep="")