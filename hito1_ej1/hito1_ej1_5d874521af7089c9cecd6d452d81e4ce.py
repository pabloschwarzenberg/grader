PT = float(input("ingrese la nota de las tareas (PT): "))
PI = float(input("ingrese la nota de las interrogaciones (PI): "))
NE = float(input("ingrese la nota del examen (NE): "))
PP = float(input("ingrese la nota de presentacion (PP): "))
  
promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
 
print("el promedio final es:", round(promedio_final, 1))
 
     