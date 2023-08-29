PT = eval(input("Ingrese la nota final de sus tareas:"))
PI = eval(input("Ingrese la nota final de sus interrogaciones:"))
NE = eval(input("Ingrese la nota final de su examen:"))
PP = eval(input("Ingrese la nota final de su presentación:"))
promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(round(promedio,1))
      