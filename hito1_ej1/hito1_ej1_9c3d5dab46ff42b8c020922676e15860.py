#Nota final
PT = float(input("ingrese la nota por tareas : "))
PI = float(input("ingrese la nota por interrogaciones : "))
NE = float(input("ingrese la nota por examen : "))
PP = float(input("ingrese la nota por presentacion : "))

PF = float(0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)

round(PF)
print("el promedio del alumno es : ", PF)