print("Ingrese en las siguientes filas sus notas: ")

pi=float(input("Promedio de Interrogaciones: "))
pt=float(input("Promedio de Tareas: "))
ne=float(input("Nota de Examen: "))
pp=float(input("Presentacion: "))

x=0.3*(pi+pt+ne)+0.1*pp

print("Tu nota final es: ",round(x,1))


      