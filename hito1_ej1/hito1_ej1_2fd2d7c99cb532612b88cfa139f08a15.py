#Nota final
PT=float(input("Ingrese la nota de Tareas: "))
PI=float(input("Ingrese la nota de Interrogaciones: "))
NE=float(input("Ingrese la nota de Examen: "))
PP=float(input("Ingrese la nota de Presentacion: "))

NotaFinal= PT*0.3+PI*0.3+NE*0.3+PP*0.1

print("Su promedio final es: ",round(NotaFinal,1))