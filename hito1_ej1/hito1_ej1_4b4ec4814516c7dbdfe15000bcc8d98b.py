#Nota final
PT=(float(input("Ingrese  su nota de tareas: ")))
PI=(float(input("Ingrese su nota de Interrogaciones: ")))
NE=(float(input("Ingrese su nota de Examen: ")))
PP=(float(input("Ingrese su nota de Presentacion: ")))

print(round((0.3*PT+0.3*PI+0.3*NE+0.1*PP),1))