#Nota final
print("Se le pedirá ingresar cuatro notas: Tareas, Interrogaciones, Examen y Presentación. El programa mostrará el promedio de sus notas, redondeado a un decimal.")
ntpt=float(input("Ingrese su nota de Tareas: "))
ntpi=float(input("Ingrese su nota de Interrogaciones: "))
ntne=float(input("Ingrese su nota de Examen: "))
ntpp=float(input("Ingrese su nota de Presentación: "))
prom=round((ntpt*0.3)+(ntpi*0.3)+(ntne*0.3)+(ntpp*0.1), 1)
print("Su promedio final es: ",prom)