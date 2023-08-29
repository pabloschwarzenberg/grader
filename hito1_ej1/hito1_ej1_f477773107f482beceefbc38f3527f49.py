#Nota final
      #PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion
PT = float(input("Ingrese nota TAREAS: "))
PI = float(input("Ingrese nota INTERROGACIONES: "))
NE = float(input("Ingrese nota EXAMÉN: "))
PP = float(input("Ingrese nota PRESENTACIÓN: "))

promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("El promedio de las 4 notas son: ",round(promedio,1))