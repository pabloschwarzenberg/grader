#Nota final
 PT = int(input("escriba la nota de las tareas: " ))
PI = int(input("escriba la nota de las interrogaciones: " ))
NE = int(input("escriba la nota del examen: " ))
PP = int(input("escriba la nota de la presentacion: " ))

a = PT * 0.3
b = PI * 0.3
c = NE * 0.3
d = PP * 0.1

promedio = round(a + b + c + d, 1)

print("tu promedio es: ", promedio)