#Nota final
#entrada
PT = float(input("Introduzca la nota de las TAREAS: "))
PI = float(input("Introduzca la nota de las INTERROGACIONES: "))
NE = float(input("Introduzca la nota del EXAMEN: "))
PP = float(input("Introduzca la nota de la PRESENTACIÓN: "))

#proceso
PT_final = PT * 0.3
PI_final = PI * 0.3
NE_final = NE * 0.3
PP_final = PP * 0.1

avg = PT_final + PI_final + NE_final + PP_final

print("El promedio final es: ", round(avg, 1))