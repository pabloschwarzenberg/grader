#Nota final
PT=float(input("Ingresa tu nota de Tareas: "))
PI=float(input("Ingresa tu nota de Interrogaciones: "))
NE=float(input("Ingresa tu nota de Examen: "))
PP=float(input("Ingresa tu nota de Presentacion: "))

tareas= 0.3*PT
interrogaciones=+0.3*PI
examen=0.3*NE
presentacion=0.1*PP

promedio=(tareas+interrogaciones+examen+presentacion)

print("La nota final es: ", "{:.1f}". format(promedio))
