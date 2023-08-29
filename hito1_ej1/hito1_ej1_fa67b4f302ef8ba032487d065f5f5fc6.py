#Nota final
PT = float(input("ingrese la nota de las tareas --> "))
PI = float(input("ingrese la nota de las interrogaciones --> "))
NE = float(input("ingrese la nota del examen --> "))
PP = float(input("ingrese la nota de presentacion -->"))

print(round(0.3*PT+0.3*PI+0.3*NE+0.1*PP, 1))      