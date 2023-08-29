#Nota final
PT = eval(input("Ingrese las notas de tareas :"))
PI = eval(input("Ingrese las notas de interrogacion :"))
NE = eval(input("Ingrese las notas de examen :"))
PP = eval(input("Ingrese las notas de presentacion :"))
 
tareas = 0.3*PT
interrogacion = 0.3*PI
examen = 0.3*NE
presentacion = 0.1*PP

promedio = tareas + interrogacion + examen + presentacion

print(round(promedio,1))