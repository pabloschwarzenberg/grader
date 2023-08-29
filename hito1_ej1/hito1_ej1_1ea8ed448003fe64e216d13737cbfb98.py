#Nota final
PT= float(input("Su nota de TAREAS: "))
PI= float(input("Su nota de INTERROGACIONES: "))
NE= float(input("Su nota de EXAMENES: "))
PP= float(input("Su nota de PRESENTACIÓN: "))

prome_fin= 0.3 * PT + 0.3 * PI + 0.3* NE + 0.1* PP
#result
print("Promedio final es: ",round(prome_fin,1))
