#salida : Nota final
#entrada: PT, PI, NE, PP,
#1. obtener PT
PT = float(input(" ingresa PT : "))
#2. obtener PI
PI = float(input(" ingresa PI : "))
#3. obtener NE
NE = float(input(" ingresa NE : "))
#4. obtener PP
PP = float(input(" ingresa PP : "))
#9. nota presentacion
nota =  0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print ("nota de presentacion: ",round(nota ,1))