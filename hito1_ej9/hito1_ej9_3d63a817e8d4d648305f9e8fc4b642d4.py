#Sistema de Ecuaciones
print("Para la siguiente ecuación ingrese los valores de 'x', 'y' y 'n'")
print("x+y=n")

x_1 = int(input("Ingrese el valor de x en la primera ecuación: "))
y_1 = int(input("Ingrese el valor de y en la primera ecuación: "))
n_1 = int(input("Ingrese el valor de n en la primera ecuación: "))

x_2 = int(input("Ingrese el valor de x en la segunda ecuación: "))
y_2 = int(input("Ingrese el valor de y en la segunda ecuación: "))
n_2 = int(input("Ingrese el valor de n en la segunda ecuación: "))

#Creación de ecuaciones
ec_uno =(str(x_1) + "X + " + str(y_1) + "Y = " + str(n_1))
ec_dos =(str(x_2) + "X + " + str(y_2) + "Y = " + str(n_2))

print("La ecuación 1 es: ", (ec_uno))
print("La ecuación 2 es: ", (ec_dos))

#Evaluación
x = (n_2-(y_2*(x_1*n_2-(n_1*x_2))/(x_1*y_2-(y_1*x_2))))/x_2
x = round(x,1)

y = (x_1*n_2-(n_1*x_2))/(x_1*y_2-(y_1*x_2))
y = round(y,1)

#Salida
print("x = ", x)
print("y = ", y)