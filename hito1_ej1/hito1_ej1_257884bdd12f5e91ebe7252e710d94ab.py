PT = float(input("nota de tareas: "))
PI = float(input("nota de interrogaciones: "))
NE = float(input("nota de examen: "))
PP = float(input("nota de presentaciones : "))
nota_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("nota final: ", round(nota_final,1))     