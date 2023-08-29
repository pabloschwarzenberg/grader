#Nota final

print("Recuerde ingresar el decimal de sus notas con un \".\"")
PT = float(input("Ingrese su nota de Tareas: "))
PI = float(input("Ingrese su nota de Interrogaciones: "))
NE = float(input("Ingrese su nota de Examen: "))
PP = float(input("Ingrese su nota de Presentación: "))

calculo = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)

print("Su promedio final es: {}".format(round(calculo, 1)))