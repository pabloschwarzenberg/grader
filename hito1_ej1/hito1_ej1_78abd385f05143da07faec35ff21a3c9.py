#Nota final
PT= float(input("Ingresa la nota de Tareas (PT): "))
PI= float(input("Ingresa la nota de Interrogaciones (PI): "))
NE= float(input("Ingresa la nota de Examen (NE): "))
PP= float(input("Ingresa la nota de Presentacion (PP): "))

promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
round(promedio_final, 1)

# Imprimir el resultado
print("El promedio final es:", promedio_final)