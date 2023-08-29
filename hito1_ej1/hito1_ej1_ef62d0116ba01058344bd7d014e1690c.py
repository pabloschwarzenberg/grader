#Nota final
#Ingreso de Notas

pt=float(input("Porfavor Ingrese la nota de Tareas: "))
pi=float(input("Ingrese la nota de Interrogaciones: "))
ne=float(input("Ingrese la nota de Examen: "))
pp=float(input("Ingrese la nota de Presentacion "))

#Desarrollo promedio final

promedio_final= 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp

#redondeo


print("Promedio final es: ", round(promedio_final, 2))

