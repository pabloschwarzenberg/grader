#Nota final
#Pedir datos al usuario:
PT = float(input("Ingresar la nota correspondiente a TAREAS: "))
PI = float(input("Ingresar la nota correspondiente a INTERROGACIONES: "))
NE = float(input("Ingresar la nota correspondiente a EXAMEN: "))
PP  = float(input("Ingresar la nota correspondiente a PRESENTACION: "))

#Imprimir resultado de formula:
print("Tu nota es: " + str(round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP, 1)))