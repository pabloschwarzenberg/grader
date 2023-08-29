#Nota final
from math import trunc

PT = eval(input("Ingrese la nota de tareas: "))
PI = eval(input("Ingrese la nota de la interrogacion: "))
NE = eval(input("Ingrese la nota del examen: "))
PP = eval(input("Ingrese la nota de la presentacion: "))

NF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
NF = NF * 10
NF = trunc(NF)
NF = NF / 10
print("Nota Final: " , NF)
   