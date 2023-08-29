def calcular_promedio_final(PT, PI, NE, PP):
    promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(promedio_final, 1)

# Solicitar las cuatro notas al usuario
PT = float(input("Ingrese la nota de PT (Tareas): "))
PI = float(input("Ingrese la nota de PI (Interrogaciones): "))
NE = float(input("Ingrese la nota de NE (Examen): "))
PP = float(input("Ingrese la nota de PP (Presentacion): "))

# Calcular el promedio final
promedio = calcular_promedio_final(PT, PI, NE, PP)

# Imprimir el resultado
print("El promedio final es:", promedio)