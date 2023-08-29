#Nota final
PT = float(input("Ingrese la nota de Tareas: "))

PI = float(input("Ingrese la nota de Interrogaciones: "))

NE = float(input("Ingrese la nota de Examen: "))

PP = float(input("Ingrese la nota de la Presentación: "))

               
promedio = ((PT*0.3) + (PI*0.3) + (NE*0.3) + (PP*0.1))

print("El promedio final es:",round(promedio,1))
    