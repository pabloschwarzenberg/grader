#Nota final hito

PT = float(input("Ingrese la nota de las tareas >>> "))
PI = float(input("Ingrese la nota de las interrogaciones >>> "))
NE = float(input("Ingrese la nota de los examenes >>> "))
PP = float(input("Ingrese la nota de las presentaciones >>> "))

PTR = round(PT, 1)
PIR = round(PI, 1)
NER = round(NE, 1)
PPR = round(PP, 1)
Promedio = (0.3 * PTR) + (0.3 * PIR) + (0.3 * NER) + (0.1 * PIR)

PromedioF = round(Promedio, 1)

print(PromedioF)