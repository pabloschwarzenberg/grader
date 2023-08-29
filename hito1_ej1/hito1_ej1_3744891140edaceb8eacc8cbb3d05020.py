#Nota final
notaPT = float(input("Ingrese nota de tareas(PT): "))
notaPI = float(input("Ingrese nota de interrogaciones(PI): "))
notaNE = float(input("Ingrese nota de exámen(NE): "))
notaPP = float(input("Ingrese nota de presentación(PP): "))

promedio = (notaPT * 0.3) + (notaPI * 0.3) + (notaNE * 0.3) + (notaPP * 0.1)
promedio = round(promedio, 1)

print(promedio)      