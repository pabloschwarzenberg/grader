#Aprobación de créditos
I = int(input("Ingrese ingreso en pesos"))
AN = int(input("ingrese año de nacimiento"))
NH = int(input("Ingrese número de hijos"))
AP = int(input("Ingrese años de pertenencia en el banco"))
EC = str(input("Ingrese estado civil. S: Soltero , C: Casado"))
V = str(input("Inrese lugar de residencia. U : Urbano, R: Rural"))

if AP > 10 and NH >= 2:
    print("APROBADO")

elif EC == "S" and NH > 3 and (AN >= 1973 and AN <= 1963):
    print("APROBADO")

elif I > 2500000 and EC == "S" and V == "U":
    print("APROBADO")

elif I > 3500000 and AP > 5:
    print ("APROBADO")

elif V == "R" and EC == "C" and NH < 2:
    print("APROBADO")
    
else:
    print("RECHAZADO")     