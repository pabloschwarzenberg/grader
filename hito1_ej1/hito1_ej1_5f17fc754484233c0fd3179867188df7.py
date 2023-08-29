def calcular_promedio_final(PT, PI, NE, PP):
    promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(promedio_final, 1)

# Solicitamos al usuario que ingrese las cuatro notas
PT = float(input("Ingrese la nota de Tareas (PT): "))
PI = float(input("Ingrese la nota de Interrogaciones (PI): "))
NE = float(input("Ingrese la nota de Examen (NE): "))
PP = float(input("Ingrese la nota de Presentación (PP): "))

# Calculamos el promedio final utilizando la función calcular_promedio_final
promedio = calcular_promedio_final(PT, PI, NE, PP)

# Imprimimos el resultado redondeado a un decimal
print("El promedio final es:", promedio)
