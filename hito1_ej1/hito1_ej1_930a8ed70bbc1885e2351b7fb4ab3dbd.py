#Nota final
## Realiza un programa para preguntar al usuario cuatro notas:

#PT = Tareas
#PI = Interrogaciones
#NE = Examen
#PP = Presentacion
##Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP
##Imprime el resultado redondeado a un decimal.
##Entrada de datos
pt = int(input("Ingrese la primera nota de TAREAS {PT}: "))
pi = int(input("Ingrese la primera nota de INTERROGACIONES {PI}: "))
ne = int(input("Ingrese la primera nota de EXAMENES {NE}: "))
pp = int(input("Ingrese la primera nota de PRESENETACIONES {PP}: "))
promf = pt*0.3 + pi*0.3 + 0.3*ne + 0.1*pp
print(round(promf,2))