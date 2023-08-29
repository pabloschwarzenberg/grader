#Nota final

PT = float(input("ingrese la nota de la tarea:"))
PI = float(input("ingrese la nota de Interrogaciones:"))
NE= float(input("ingrese la nota del Examen:"))
PP = float(input("ingrese la nota de la Presentacion:"))

x= float(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

print("promedio de notas redondeado a decimal", x)