#Nota final
PT = float(input("Indique su nota de tareas(PT): "))
PI = float(input("Indique su nota de interrogaciones(PI): "))
NE = float(input("Indique su nota de examen(NE): "))
PP = float(input("Indique su nota de presentación(PP): "))

promedio = 0.3*PT+0.3*PI+0.3*NE+0.1*PP

print("Su promedio final es de: ",round(promedio, 1))