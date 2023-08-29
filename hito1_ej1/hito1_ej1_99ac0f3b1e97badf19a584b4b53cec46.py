#Nota final
PT = eval(input("Ingrese la nota de tareas: "))
PI = eval(input("Ingrese la nota de interrogaciones: "))
NE = eval(input("Ingrese la nota del examen: "))
PP = eval(input("Ingrese la nota de la presentación: "))

PT_final = PT * 0.3
PI_final = PI * 0.3
NE_final = NE * 0.3
PP_final = PP * 0.1

promedio = PT_final + PI_final + NE_final + PP_final

print("El promedio de sus notas es: ", promedio)
