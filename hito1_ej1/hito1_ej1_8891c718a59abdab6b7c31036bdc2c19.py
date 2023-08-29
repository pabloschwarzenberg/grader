#Nota final
      
PT=eval(input("Ingrese nota de Tareas: "))
PI=eval(input("Ingrese nota de Interrogaciones: "))
NE=eval(input("Ingrese nota de Examen: "))
PP=eval(input("Ingrese nota de Presentación: "))

prom= (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("El promedio de sus notas es: ",prom)