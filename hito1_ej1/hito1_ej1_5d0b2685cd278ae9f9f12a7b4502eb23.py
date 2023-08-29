#Nota final
print("Introduce tus notas:")
tareas=float(input("Nota de Tareas:"))
interrogaciones=float(input("Nota de Interrogaciones:"))
examen=float(input("Nota de Exámen:"))
presentacion=float(input("Nota de Precentación:"))
c=float(round((0.3*tareas+0.3*interrogaciones+0.3*examen+0.1*presentacion),1))
print("Tu promedio es:",c)