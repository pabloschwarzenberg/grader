#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
    promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    promedio_final_redondeado = round(promedio_final, 1)  

    
    print("El promedio final es:", promedio_final_redondeado)
PT = float(input("Ingrese la nota de las Tareas: "))
PI = float(input("Ingrese la nota de las Interrogaciones: "))
NE = float(input("Ingrese la nota del Examen: "))
PP = float(input("Ingrese la nota de la Presentación: "))
calcular_promedio_final(PT, PI, NE, PP)
      