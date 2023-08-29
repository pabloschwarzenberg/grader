# nota final
# Entrada
PT= float(input("Ingresa tu nota por tareas: "))
PI= float(input("Ingresa tu nota por interrogaciones: "))
NE= float(input("Ingresa tu nota del examen: "))
PP= float(input("Ingresa tu nota de la presentacion: "))
# Procesamiento
Nota_final= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
# Salida
print("La nota final del curso es: ", round(Nota_final, 1))