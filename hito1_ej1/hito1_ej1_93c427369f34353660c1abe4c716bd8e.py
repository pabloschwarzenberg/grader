PT = eval(input("Que nota tienes en las Tareas?: "))
PI = eval(input("Que nota tienes en las Interrogaciones?: "))
NE = eval(input("Que nota tienes en las Examen?: "))
PP = eval(input("Que nota tienes en las Presentacion?: "))
nota_f= 3/10*PT + 3/10*PI + 3/10*NE + 1/10*PP
print(round(nota_f,1))