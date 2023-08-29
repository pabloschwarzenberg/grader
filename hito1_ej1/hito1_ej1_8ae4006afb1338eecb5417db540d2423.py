#Nota final

print("Debe ingresar las notas solicitadas de tareas, interrogaciones, examen y nota de presentacion")
PT = float(input("ingrese la nota de tareas: "))
PI = float(input("ingrese la nota de interrogaciones: "))
NE = float(input("ingrese la nota de examen: "))
PP = float(input("ingrese la nota de presentacion del alumno"))

PF = round (((0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)),1)

print (("su promedio final de la asignatura es: " + (str(PF))))