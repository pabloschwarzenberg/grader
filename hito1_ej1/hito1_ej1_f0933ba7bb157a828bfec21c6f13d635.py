#Entrada
PT = float(input("Ingrese Nota de Puntaje de Tareas: "))
PI = float(input("Ingrese Nota de Puntaje de Interrogantes: "))
NE = float(input("Ingrese Nota de Examen: "))
PP = float(input("Ingrese Nota de Presentación: "))

#Condiciones

Resultado = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP) 

#Final
print("La Nota final es", Resultado)
      