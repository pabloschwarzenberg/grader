#Nota final
PT = float(input("pon tu puntaje tareas"))
PI = float(input("pon tu puntaje interrogaciones"))
NE = float(input("puntaje examen"))
PP = float(input("puntaje presentacion"))
print(round( 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP , 1 ))