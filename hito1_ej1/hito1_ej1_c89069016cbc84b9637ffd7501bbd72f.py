#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
    promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(promedio, 1)

# Solicitar al usuario ingresar las cuatro notas
PT = float(input("Ingrese la nota de las Tareas (PT): "))
PI = float(input("Ingrese la nota de las Interrogaciones (PI): "))
NE = float(input("Ingrese la nota del Examen (NE): "))
PP = float(input("Ingrese la nota de la Presentación (PP): "))

# Calcular el promedio final
promedio_final = calcular_promedio_final(PT, PI, NE, PP)

# Imprimir el resultado redondeado a un decimal
print("El promedio final es:", promedio_final)
   