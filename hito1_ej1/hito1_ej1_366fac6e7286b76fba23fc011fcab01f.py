PT = float(input("Ingrese nota por tareas:"))
PI = float(input("Ingrese nota por interrogaciones:"))
NE = float(input("Ingrese nota por examen:"))
PP = float(input("Ingrese nota presentación:"))
promedio = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
promediofinal = round(promedio,1)
print("el promedio final es:",promediofinal)
