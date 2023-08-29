#Nota final
 # Solicitamos las notas al usuario
PT = float(input("Ingresa la nota de Tareas: "))
PI = float(input("Ingresa la nota de Interrogaciones: "))
NE = float(input("Ingresa la nota de Examen: "))
PP = float(input("Ingresa la nota de Presentacion: "))

# Calculamos la nota final según la fórmula proporcionada
nota_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

# Imprimimos el resultado redondeado a un decimal
print(round(nota_final, 1))
     