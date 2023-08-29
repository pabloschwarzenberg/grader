#Nota final

#Entradas

PT = float(input("Ingrese su nota de Tareas: "))
PI = float(input("Ingrese su nota de Interrogaciones: "))
NE = float(input("Ingrese su nota de Examen: "))
PP = float(input("Ingrese su nota de Presentacion: "))

#Desarrollo

NF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

#Salidas

print("Su nota final es: " , "{:.1f}".format(NF))