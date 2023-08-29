#Nota final

PT = eval(input("Ingrese su nota de Tareas: "))
PI = eval(input("Ingrese su nota de Interrogación: "))
NE = eval(input("Ingrese su nota de Examen: "))
PP = eval(input("Ingrese su nota de Presentación: "))

NF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
round(NF)

print("tu nota final es: {}".format(NF))