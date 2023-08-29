#Nota final

#Entradas
PT = float(input("ingrese su promedio de tareas: "))
PI = float(input("ingrese su promedio de interrogaciones: "))
NE = float(input("ingrese su nota de examen: "))
PP = float(input("ingrese su promedio de presentaciones: "))
NF = 0

#Calculo
NF = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
      
#Salida
print("El promedio final es:", round(NF, 1))
print("FIN.")
      