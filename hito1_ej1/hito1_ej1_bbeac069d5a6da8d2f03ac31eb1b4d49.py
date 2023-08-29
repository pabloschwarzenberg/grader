#Preguntas

#PT = Tareas
#PI = Interrogantes
#NE = Examen
#PP = Presentacion

PT = float(input("Nota de tarea= "))
PI = float(input("Nota de Interrogantes= "))
NE = float(input("Nota de Examen= "))
PP = float(input("Nota de Presentacion= "))

#Nota final

notaFinal = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
SinDecimal = int(notaFinal*100)
Resto = SinDecimal % 10

#Comprobacion
if Resto >= 5 :
    SinDecimal -= Resto
    SinDecimal += 10
elif Resto < 5 :
    SinDecimal -= Resto

#Resultado

Promedio = SinDecimal / 100
print(Promedio)