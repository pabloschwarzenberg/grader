#Nota final
PT=float(input("Ingrese su nota de Tareas: "))
PI=float(input("Ingrese su nota de Interrogaciones: "))
NE=float(input("Ingrese su nota de Examen: "))
PP=float(input("Ingrese su nota de Presentación: "))
PF=(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
PF=(round(PF,1))
print("Su Promedio Final es: ", PF)
print("Su Promedio Final es %.1f" % (PF))