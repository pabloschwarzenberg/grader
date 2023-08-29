#Nota final
print("calculo de notas")
PT = float(input("ingrese su nota de tareas:" + " "))
PI = float(input("ingrese su nota de interrogaciones:" + " "))
NE = float(input("ingrese su nota de examen:" + " "))
PP = float(input("ingrese su nota de presentacion:" + " "))
x = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print ("su promedio es:", " ", str(round (x,1)))