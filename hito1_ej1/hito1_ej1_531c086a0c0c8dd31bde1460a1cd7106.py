#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
    promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    promedio_redondeado = round(promedio, 1)
    return promedio_redondeado

# Solicitar las cuatro notas al usuario
PT = float(input("Ingrese la nota de Tareas (PT): "))
PI = float(input("Ingrese la nota de Interrogaciones (PI): "))
NE = float(input("Ingrese la nota de Examen (NE): "))
PP = float(input("Ingrese la nota de Presentacion (PP): "))

# Calcular el promedio final
promedio_final = calcular_promedio_final(PT, PI, NE, PP)

# Imprimir el resultado redondeado a un decimal
print("El promedio final es:", promedio_final)
      