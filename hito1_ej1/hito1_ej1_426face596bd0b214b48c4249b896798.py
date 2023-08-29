#Nota final
PT = float(input("Ingrese la nota de tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones: "))
NE = float(input("Ingrese la nota de Examenes: "))
PP = float(input("Ingrese la nota de Presentación: "))

promedio = PT*0.3 + PI*0.3 + NE*0.3 + PP*0.1

print("Su promedio es: ",round(promedio, 1))