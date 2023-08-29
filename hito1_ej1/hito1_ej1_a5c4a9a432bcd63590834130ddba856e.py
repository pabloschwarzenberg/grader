# solicitar ingreso de notas
PT = float(input("ingresar nota de tareas: "))
PI = float(input("ingresar nota de interrogracion:"))
NE = float(input("ingresar nota del examen: "))
PP = float(input("ingresar nota de presentacion: "))
#resultado promedio final
promedio_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

#REDONDEAR PROMEDIO FINAL
promedio = round(promedio_final,1)

print(promedio)