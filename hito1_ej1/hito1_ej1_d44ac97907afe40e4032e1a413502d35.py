#Nota final
PT = eval(input("Ingrese la nota promedio de sus tareas: "))
PI = eval(input("Ingrese la nota promedio de sus interrogaciones: "))
NE = eval(input("Ingrese la nota promedio de sus exámenes: "))
PP = eval(input("Ingrese la nota promedio de sus presentaciones: "))
promedio = (0.3*(PT))+(0.3*(PI))+(0.3*(NE))+(0.1*(PP))
print("Su promedio final es : "+ str(round(promedio,10)))