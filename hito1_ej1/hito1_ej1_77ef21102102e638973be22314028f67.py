#Nota final
#Realiza un programa para preguntar al usuario cuatro notas:
#PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion
#Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP Imprime el resultado redondeado a un decimal.
#entrada:
pt=float(input("nota de tareas:"))
pi=float(input("nota de interrogaciones:"))
ne=float(input("Examen:"))
pp=float(input("presentaciones:"))
#desarrollo:
notaf=0.3*pt+0.3*pi+0.3*ne+0.1*pp
print(round(notaf,1))