#Nota final
PT=float(input("Intrduzca su nota de Tareas: "))
PI=float(input("Introduzca su nota de Interrogacaciones: "))
NE=float(input("Introduzca su nota del Exámen: "))
PP=float(input("Intrdozuca su nota de Presentación: "))
print("Estamos calculando su promedio...")
promedio=((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP))
print("Su nota final es:", round(promedio,1))     