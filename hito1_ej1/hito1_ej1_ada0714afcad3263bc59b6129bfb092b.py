#Nota final
PT = eval(input("Nota Tareas: "))
PI = eval(input("Nota Interrogaciones: "))
NE = eval(input("Nota Examen: "))
PP = eval(input("Nota Presentaciones : "))

nota_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("La nota final es:", round(nota_final,1))