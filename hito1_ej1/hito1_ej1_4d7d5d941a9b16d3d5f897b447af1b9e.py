#Nota final

PorcentajePT = 0.3
PorcentajePI = 0.3
PorcentajeNE = 0.3
PorcentajePP = 0.1


Nota1 = (input("Inserte nota PT : "))
Nota2 = (input("Inserte nota PI : "))
Nota3 = (input("Inserte nota NE : "))
Nota4 = (input("Inserte nota PP : "))

PctjeNota1 = (float(Nota1) * float(PorcentajePT))
PctjeNota2 = (float(Nota2) * float(PorcentajePI))
PctjeNota3 = (float(Nota3) * float(PorcentajeNE))
PctjeNota4 = (float(Nota4) * float(PorcentajePP))

Promedio = (PctjeNota1 + PctjeNota2 + PctjeNota3 + PctjeNota4)
format_float = "{:.1f}".format(Promedio)
print ("Su promedio de la asignatura es : " ,format_float)