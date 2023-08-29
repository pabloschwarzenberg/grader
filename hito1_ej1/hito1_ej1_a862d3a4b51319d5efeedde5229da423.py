#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
    promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    promedio_redondeado = round(promedio, 1)
    print("El promedio final es:", promedio_redondeado)

# Pedir al usuario que ingrese las cuatro notas
PT = float(input("Ingrese la nota de PT (Tareas): "))
PI = float(input("Ingrese la nota de PI (Interrogaciones): "))
NE = float(input("Ingrese la nota de NE (Examen): "))
PP = float(input("Ingrese la nota de PP (Presentacion): "))

# Llamar a la función para calcular e imprimir el promedio final redondeado
calcular_promedio_final(PT, PI, NE, PP)
