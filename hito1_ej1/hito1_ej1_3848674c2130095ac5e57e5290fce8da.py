#Nota final
PT = float(input(("Ingrese la nota de las ""Tareas"": ")))
PI = float(input(("Ingrese la nota de las ""Interrogaciones"": ")))
NE= float(input(("Ingrese nota del ""Examen"": ")))
PP = float(input(("Ingrese la nota de la ""Presentacion"": ")))

NF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print(round(NF,1))