#Nota final
import math
PT= float(input("Inserte nota de Tareas"))
PI= float(input("Inserte nota de interrogaciones"))
NE= float(input("Inserte nota de Examen"))
PP= float(input("Inserte nota de presentacion"))
suma=( 0.3*PT  + 0.3*PI + 0.3*NE + 0.1*PP)
round(suma, 1)
print(suma)