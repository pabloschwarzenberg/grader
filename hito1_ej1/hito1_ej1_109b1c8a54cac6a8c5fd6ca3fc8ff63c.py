#Nota final
PT=float(input("Ingrese el promedio de tareas "))
PI=float(input("ingrese el promedio de las interrogaciones "))
NE=float(input("ingrese su nota del examen "))
PP=float(input("ingrese su nota de presentacion "))
promedio = 0.3*PT+0.3*PI+0.3*NE+0.1*PP
promedio_redondeado=round(promedio,1)
print("Su promedio es ",promedio_redondeado)
          