#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
    promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    promedio_redondeado = round(promedio, 1)
    return promedio_redondeado

# Pedir al usuario que ingrese las notas
PT = float(input("Ingrese la nota de PT: "))
PI = float(input("Ingrese la nota de PI: "))
NE = float(input("Ingrese la nota de NE: "))
PP = float(input("Ingrese la nota de PP: "))

# Calcular el promedio final
promedio_final = calcular_promedio_final(PT, PI, NE, PP)

# Imprimir el resultado
print("El promedio final es:", promedio_final)
