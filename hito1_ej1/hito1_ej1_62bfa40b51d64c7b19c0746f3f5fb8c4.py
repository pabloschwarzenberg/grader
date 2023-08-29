#Nota final
PT = float(input("ingrese la nota de tareas:"))
PI = float(input("ingrese su nota de interrogaciones:"))
NE = float(input("ingrese su nota de examenes:"))
PP = float(input("ingrese su nota de asistencias:"))

nota = PT*0.3 + PI*0.3 + NE*0.3 + PP*0.1
print("la nota final del curso es:", round(nota,1))