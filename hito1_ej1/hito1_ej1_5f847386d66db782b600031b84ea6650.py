#Nota final
print("ingrese las cuatro notas:")
PT = float(input("la nota de tarea es: "))
PI = float(input("la nota de interrogaciones es: "))
NE = float(input("la nota de examens es: "))
PP = float(input("la nota de presentaciones es: "))
Z = ((0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP))
Z = round(Z,1)
print("el promedio redondeado es: ", Z)