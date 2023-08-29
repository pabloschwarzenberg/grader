#Nota final
PT = float(input("Ingrese nota Tareas: "))
Pl = float(input("Ingrese nota Interrogaciones: "))
NE = float(input("Ingrese nota Examen: "))
PP = float(input("Ingrese nota Presentación: "))

zzz = ((PT*0.3)+(Pl*0.3)+(NE*0.3)+(PP*0.1))
print("Su Promedio Final es:" , round(zzz , 1))