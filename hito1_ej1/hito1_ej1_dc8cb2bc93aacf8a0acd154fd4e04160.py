#Nota final

PT = eval(input("Ingrese su nota de las tareas: "))
PI = eval(input("Ingrese su nota de las interrogaciones: "))
NE = eval(input("Ingrese su nota del examen: "))
PP = eval(input("Ingrese su nota de la presentación: "))

Nota_Presentación = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("Su nota de presentación es: %.1f" %(Nota_Presentación))