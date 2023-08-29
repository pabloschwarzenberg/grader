#Nota final
def calcular_promedio_final():
    PT = float(input("Ingrese nota de PT: "))
    PI = float(input("Ingrese nota de PI: "))
    NE = float(input("Ingrese nota de NE: "))
    PP = float(input("Ingrese nota de PP: "))
    promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP 
    print("El promedio final es:", round(promedio_final, 1))
calcular_promedio_final()