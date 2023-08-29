#Nota final
PT = float(input("Ingresa Nota Tareas: "))
PI = float(input("Ingresa Nota Interrogaciones: "))
NE = float(input("Ingresa Nota Examen: "))
PP = float(input("Ingresa Nota Presentación: "))
PF = round((PT*0.3)+(PI*0.3)+(NE*0.3)+(PP*0.1),1)
print("El promedio final es:",str(PF))      