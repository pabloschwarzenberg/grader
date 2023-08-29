#Nota final
PT = float(input("Introduce la nota de la tarea: "))
PI = float(input("Introduce la nota de la interrogacion: "))
NE = float(input("Introduce la nota del examen: "))
PP = float(input("Introduce la nota de la presentacion: "))

promedio = (PT*0.3)+(PI*0.3)+(NE*0.3)+(PP*0.1)
promedio = round(promedio ,1) 
print(promedio)   