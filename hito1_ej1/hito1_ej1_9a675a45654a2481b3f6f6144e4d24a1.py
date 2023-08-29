#Nota final
PT = eval(input("Ingrese la nota de tareas: "))
PI = eval(input("Ingrese la nota de interrogaciones: "))
NE = eval(input("ingrese la nota de examen: "))
PP = eval(input("ingrese la nota de presentación: "))

promedio = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.3 * PP)
redondeo = round(promedio,1)

print("Tu promedio final es",redondeo)
      