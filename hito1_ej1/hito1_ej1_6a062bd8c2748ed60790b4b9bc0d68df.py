#Nota final
def CPF(PT, PI, NE, PP):
    PF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(PF, 1)

PT = float(input("Ingrese la nota de las Tareas (PT): "))
PI = float(input("Ingrese la nota de las Interrogaciones (PI): "))
NE = float(input("Ingrese la nota del Examen (NE): "))
PP = float(input("Ingrese la nota de la Presentación (PP): "))


promediofinal = CPF(PT, PI, NE, PP)

print("El promedio final es:", promediofinal)     