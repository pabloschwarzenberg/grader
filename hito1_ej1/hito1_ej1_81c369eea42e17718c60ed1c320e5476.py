#Nota final
PT = eval(input("Introduzca su nota de tareas: "))
PI = eval(input("Ingrese su nota de interrogaciones: "))
NE = eval(input("Ingrese su nota de Examen: "))
PP = eval(input("Ingrese su nota de Presentacion: "))

PF = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
PF = PF.__round__(1)
print("su promedio final es: {0}".format(PF))