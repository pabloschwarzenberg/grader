I = float(input("Ingrese su ingreso en pesos ->"))
F = int(input("Ingrese su año de nacimiento ->"))
H = int(input("Ingrese la cantidad de Hijos ->"))
AP = int(input("Ingrese la cantidad de años que pertenece al banco->"))
ES =input ("Ingrese estado civil si es  S o C: ")
V = input("Ingrese si vive en un lugar R o U: ")
edad = 2021 - F


if   AP>10 and H>=2: 
                condicion= "APROBADO "

elif  ES == "C" and H>3 and edad <55 and edad >45 :
                condicion = "APROBADO "

elif ES == "S"  and I >2500000 and V == "U" :
              condicion = "APROBADO "
 
elif I >3500000 and AP > 5:
                condicion = "APROBADO " 

elif    V == "R"  and ES == "C"  and H<2 :
                condicion = "APROBADO"

else :
                  condicion = "RECHAZADO"

print (" su credito  esta " , condicion )