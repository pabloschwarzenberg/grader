#Nota final
A = float(input("Ingrese la nota de las tareas: "))
B = float(input("Ingrese la nota de las interrogaciones: "))
C = float(input("Ingrese la nota del examen: "))
D = float(input("Ingrese la presentacion: "))
#preguntar las notas con float para que se puedan colocar decimales
E = (A*0.3)+(B*0.3)+(C*0.3)+(D*0.1)
#multiplicar las notas por los valores pedidos y sumarlas entre
CF = round(E,1)
#colocar la suma con el round al primer decimal
print("Su promedio es", CF)
#imprimir el resultado 