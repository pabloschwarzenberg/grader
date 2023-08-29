'''Realiza un programa para preguntar al usuario cuatro notas:

PT = Tareas
PI = Interrogaciones
NE= Examen
PP = Presentacion
Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP
Imprime el resultado redondeado a un decimal.'''
print('Nota Final')
N1, N2,N3,N4=eval(input('Ingrese Nota Tareas:\t')),eval(input('Ingrese Nota Interrogaciones:\t')),eval(input('Ingrese Nota Examen:\t')),eval(input('Ingrese Nota Presentación:\t'))
#print(round(float(N1),2), N2, N3, N4)
prom=((0.3*(N1+N2+N3))+(0.1*N4))
prom=round(prom,1)
print('El primedio de notas es:\t{}'.format(prom))