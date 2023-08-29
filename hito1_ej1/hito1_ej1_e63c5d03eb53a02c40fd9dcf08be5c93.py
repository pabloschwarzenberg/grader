#Nota final
PT = eval(input("tareas:"))
PI = eval(input("interrogaciones:"))
NE = eval(input("examen:"))
PP = eval(input("presentacion:"))

# promedio de las cuatro notas
F = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("promedio de las cuatro notas", round(F,1))

      