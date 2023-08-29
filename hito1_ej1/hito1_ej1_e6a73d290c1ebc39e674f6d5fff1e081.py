#Nota final
PT = eval(input("ingrese la nota de tareas: "))
PI = eval(input("ingrese nota de interrogaciones: "))
NE = eval(input("ingrese nota de examen: "))
PP = eval(input("ingrese nota de presentaciones: "))
tareas = PT * 0.3
interrogacion = PI * 0.3
examen = NE * 0.3
presentacion = PP * 0.1
promedio = round(tareas + interrogacion + examen + presentacion,1)
print("tu promedio final es: ",promedio)
