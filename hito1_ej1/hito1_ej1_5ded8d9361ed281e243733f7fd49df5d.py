#Nota final
PT = float(input("ingrese nota PT Tareas: "))
PI = float(input("ingrese nota PI Interrogaciones: "))
NE = float(input("ingrese nota NE Examen: "))
PP = float(input("ingrese nota PP Presentación: "))

promedio = (PT * 0.3) + (PI * 0.3) + (NE * 0.3) + (PP * 0.1)

promedio = round(promedio, 1)

print (promedio)