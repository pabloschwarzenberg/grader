#Sistema de Ecuaciones
       
1
# Pedimos al usuario los coeficientes del sistema
2
a1 = float(input("Introduce el coeficiente de x de la primera ecuación: "))
3
b1 = float(input("Introduce el coeficiente de y de la primera ecuación: "))
4
c1 = float(input("Introduce el término independiente de la primera ecuación: "))
5
a2 = float(input("Introduce el coeficiente de x de la segunda ecuación: "))
6
b2 = float(input("Introduce el coeficiente de y de la segunda ecuación: "))
7
c2 = float(input("Introduce el término independiente de la segunda ecuación: "))
8
 
9
# Resolvemos el sistema por el método de sustitución
10
y = (c2 - a2 * c1 / a1) / (b2 - a2 * b1 / a1)
11
x = (c1 - b1 * y) / a1
12
 
13
# Imprimimos las soluciones redondeadas a un decimal
14
print("x = {:.1f}".format(x))
15
print("y = {:.1f}".format(y))
