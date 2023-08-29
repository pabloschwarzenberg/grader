#Sistema de Ecuaciones
a1 = eval(input("Ingrese a de la ecuacion 1: "))

b1 = eval(input("Ingrese b de la ecuacion 1: "))

c1 = eval(input("Ingrese c de la ecuacion 1: "))

a2 = eval(input("Ingrese a de la ecuacion 2: "))

b2 = eval(input("Ingrese b de la ecuacion 2: "))

c2 = eval(input("Ingrese c de la ecuacion 2: "))


#multiplicar por a1 todos los valores de la ecuación 2

a3 = a1*a2

b3 = a1*b2

c3 = a1*c2

#restar los valores (b1 y b3) y (c1 y c3)

restaB = b1 - b3
restaC = c1 - c3

#dividir el valor de c resultante con el de b resultante (aquí obtengo el valor de y)

y = float(round((restaC/restaB),2))

#en la ecuación 1, multiplicar el valor de y, por b1

b3 = y*b1

#restar c1 con lo resultante del paso anterior

restaB = c1 - b3

#dividir el resultado del paso anterior con a1 (aquí obtengo valor de x)

x = float(round((restaB/a1),2))

print("x=" + str(x))
print("y=" + str(y))
