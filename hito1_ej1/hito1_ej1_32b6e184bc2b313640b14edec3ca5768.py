#Nota final
#INGRESA NOTAS FINALES
PT=float(input("promedio de tareas: "))
PI=float(input("promedio de interrogaciones: "))
NE=float(input("nota del examen: "))
PP=float(input("nota de presentación"))
#CÁLCULO DE LA NOTA FINAL
Nota_final=0.3*PT +0.3*PI +0.3*NE + 0.1*PP
#REDONDEO A UN DECIMAL
Nota_final_round=round(Nota_final,1)
#OUTPUT
print("el promedio final del curso de introducción a la programación es de: ", Nota_final_round)     