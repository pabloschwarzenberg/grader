#Aprobación de créditos
I = float(input("Ingreso:"))
AN = int(input("Año de nacimiento:"))
E = AN - 2017
N = int(input("Numero de hijos:"))
AB = int(input("Años de pertenencia al banco:"))
EC = input("Estado civil:")
CC = input("Urbano o campo:")
if AB > 10 and N > 1:
    print("APROBADO")
if EC == "C" and N > 3 and E >= 45 and E <= 55:
    print("APROBADO")
if I > 2500000 and EC == "S" and CC == "U":
    print("APROBADO")
if I > 3500000 and AB > 5:
    print("APROBADO")
if CC == "R" and EC == "C" and N < 2:
    print ("APROBADO")
else:
    print("RECHAZADO")