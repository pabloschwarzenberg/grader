#Nota final
PT=eval(input("Ingrese nota de tareas: "))
PI=eval(input("Ingrese nota de interrogaciones: "))
NE=eval(input("Ingrese nota de examen: "))
PP=eval(input("Ingrese nota de presentación: "))
Notas=PT+PI+NE
Promedio= (Notas*0.3)+(PP*0.1)
print(round(Promedio,1))