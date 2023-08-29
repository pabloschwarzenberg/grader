#Nota final
PT = float(input("Ingresa la nota de la tarea: "))
PI = float(input("Ingresa la nota de la interrogacion: "))
NE = float(input("Ingresa la nota del exámen: "))
PP = float(input("Ingresa la nota de la presentación: "))

NF = (0.3*PT+0.3*PI+0.3*NE+0.1*PP)
NF = round(NF, 1)
print(NF)
