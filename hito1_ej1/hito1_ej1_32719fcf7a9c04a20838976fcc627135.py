#Nota final
a = float(input("Ingrese la nota de Tareas : "))
b = float(input("Ingrese la nota de Interrogaciones : "))
c= float(input("Ingrese la nota de Examen : "))
d = float(input("Ingrese la nota de Presentacion : "))

promedio_final = 0.3 * a + 0.3 * b + 0.3 * c + 0.1 * d

promedio_final_redondeado = round(promedio_final, 1)

print("El promedio final es:", promedio_final_redondeado)      