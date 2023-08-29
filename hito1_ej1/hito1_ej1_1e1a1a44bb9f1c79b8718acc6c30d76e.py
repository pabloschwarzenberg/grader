#Realiza un programa para preguntar al usuario cuatro notas:

#PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion
#Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP
#Imprime el resultado redondeado a un decimal.

pt = eval(input('Ingresa nota de tareas: '))

pi = eval(input('Ingresa nota de interrogaciones: '))

ne = eval(input('Ingresa nota de examen: '))

pp = eval(input('Ingresa nota de presentacion: '))



nota=(0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)


print('La nota final es:' , nota)

