#Nota final
PT = float(input("Ingrese Nota de Trabajos:"))
PI = float(input("Ingrese Nota de Interrogaciones:")) 
NE = float(input("ingrese Nota del Examen:"))
PP = float(input("ingrese Nota de Presentación:"))
  
promedio = (0.3*PT+0.3*PI+0.3*NE+0.1*PP)

print("El Promedio Final es:", promedio)