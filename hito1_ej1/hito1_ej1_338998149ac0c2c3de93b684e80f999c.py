PT = float(input("Escriba la nota de las Tareas: "))
PI = float(input("Escriba la nota de las Interrogaciones: "))
NE = float(input("Escribe la nota de los Examenes: "))
PP = float(input("Escriba la nota de los Presentaciones: "))
Notafinal =(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)

print("El promedio del alumno es: ",round(Notafinal,1))
