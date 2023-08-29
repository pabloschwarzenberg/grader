#Nota final
  
PT=float(input("Ingrese nota tareas: "))
PI=float(input("Ingrese nota Interrogaciones: "))
NE=float(input("Ingrese nota Examen: "))
PP=float(input("Ingrese nota Presentación: "))

promediofinal=0.3*PT+0.3*PI+0.3*NE+0.1*PP

print(round(promediofinal,1))