#Nota final
PT = float(input("ingrese el promedio de notas de las tareas: "))
PI = float(input("ingrese el promedio de notas de sus interrogaciones: "))
NE = float(input("ingrese su nota de examen: "))
PP = float(input("Ingrese el promedio de sus presentaciones: "))

promedio =(0.3*PT+0.3*PI+0.3*NE+0.1*PP)

print( "Su promedio final es", round(promedio,1))
