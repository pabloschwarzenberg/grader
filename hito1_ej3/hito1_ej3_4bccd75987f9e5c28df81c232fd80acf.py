#Aprobación de créditos
print("credito")
I = eval(input("ingreso:"))
AN = eval(input("año de nacimiento:"))
NH = eval(input("Numero de hijos:"))
AP= eval(input("años pertenencia:"))
EC= input("Estado civil:")
UR= input("Campo o ciudad:")


if AP > 10 and NH >= 2 or (EC == "C" and  NH > 3 and (AN >= 1975) or (AN <= 1985)) or I >2500000 and EC == "S" and UR == "U" or I > 3500000 and AP >5 or UR == "R" and EC== "C" and NH < 2:
   print("APROBADO")
else: 
   print("REPROBADO")
    