#Nota final
PT = float(input("Ingrese nota de la tarea es: "))
PI = float(input("Ingrese nota de la interrogaciones: "))
NE = float(input("Ingrese nota del examen: "))
PP = float(input("Ingrese nota de presentacion: "))

pf = ((PT*0.3)+(PI*0.3)+(NE*0.3)+(PP*0.1))
pf = round(pf,1)
print(pf)      