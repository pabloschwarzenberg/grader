#Nota final
      
PT = float(input("Ingrese su nota por tareas: "))
PI = float(input("Ingrese su nota por interrogaciones: "))
NE = float(input("Ingrese su nota por Examenes: "))
PP = float(input("Ingrese su nota por Presentaciones: "))

promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("Su promedio final es: ",promedio)
      