#Nota final
PT = eval(input("ingrese la nota de la tarea: ")) 
PI = eval(input("ingrese la nota de la interrogacion: "))
NE = eval(input("ingrese la nota del examen: "))
PP = eval(input("ingrese la nota de la presentacion: "))
NF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
NF = round(NF, 1)
print(NF)