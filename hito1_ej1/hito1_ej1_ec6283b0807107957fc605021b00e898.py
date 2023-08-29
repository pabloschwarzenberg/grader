#Nota final
print("Ingrese las notas que son requeridas: ")
PT = float(input("Notas Tareas: "))
PI = float(input("Notas Interrogaciones: "))
NE = float(input("Notas Examen: "))
PP = float(input("Notas Presentación: "))

p = (PT*0.3) + (PI*0.3) + (NE*0.3) + (PP*0.1)
r = round(p,1)
print("Tu promedio final es:",r)