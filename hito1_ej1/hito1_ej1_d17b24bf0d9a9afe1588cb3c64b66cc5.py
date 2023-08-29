#Nota final
PT = eval(input("ingrese la nota de Tarea: "))
PI = eval(input("ingrese la nota de Interrogaciones: "))
NE = eval(input("ingrese la nota del examen: "))
PP = eval(input("ingrese la nota de Presentación: "))
Promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
redondeado = round(Promedio, 1)

if (Promedio >0):
    Prom = Promedio
    print("El promedio es: {}".format(redondeado))     