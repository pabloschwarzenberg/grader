#Nota final
# Pedir al usuario que ingrese las cuatro notas
PT = float(input("Ingresa la nota de Tareas: "))
PI = float(input("Ingresa la nota de Interrogaciones: "))
NE = float(input("Ingresa la nota de Examen: "))
PP = float(input("Ingresa la nota de Presentación: "))

# Calcular la nota final
nota_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Redondear la nota final a un decimal
nota_final_redondeada = round(nota_final, 1)

# Imprimir la nota final
print("La nota final es:", nota_final_redondeada)
      