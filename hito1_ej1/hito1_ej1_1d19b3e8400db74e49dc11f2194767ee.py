#Nota final
#Pedir al usuario que ingrese las notas
PT=float(input("Ingrese la nota de tareas: "))
PI=float(input("Ingrese la nota de las interrrogaciones: "))
NE=float(input("Ingrese la nota de examen: "))
PP=float(input("Ingrese la nota de presentacion: "))

#Calcular promedio final
promedio_f=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)

promedio_f_redondeado=round(promedio_f,1)

print("El promedio final es: ",promedio_f_redondeado)     