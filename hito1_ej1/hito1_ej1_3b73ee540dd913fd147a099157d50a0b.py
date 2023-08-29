#PT = tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion

PT = 0
PI = 0
NE = 0
PP = 0

PT = float(input('Ingrese la Nota de Tareas:' ))
PI = float(input('Ingrese la Nota de Interrogacion:' ))
NE = float(input('Ingrese la Nota de Examen:' ))
PP = float(input('Ingrese la Nota de Presentacion:' ))
nota_final =  0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print ('Su nota de presentación es :', round(nota_final,1))     