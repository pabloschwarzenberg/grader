#Aprobación de créditos
      I=int(input("Ingrese sus ingresos "))
F=int(input("Ingrese su fecha de nacimiento "))
H=int(input("Ingrese números de hijos "))
B=int(input("Ingrese hace cuanto pertenece al banco "))
E=input("cual es tu estado civil es casado o soltero ")
año=2021-F
if(E == "C"):
    print("Casado")
elif(E == "S"):
    print("Soltero")
V=input("en donde vive zona rural o urbana ")
if(V == "R"):
    print("rural")
elif(V == "U"):
    print("urbana")
if((B>=10) and (H>=2)):
    print("APROBADO")
elif((E=="C") and (H>=3)) and (año>=45,año<=55):
    print("APROBADO")
elif((I>=2500000) and (E=="S") and (V=="U")):
    print("APROBADO")
elif((I>=3500000) and (B>=5)):
    print("APROBADO")
elif((V=="R") and (E=="C") and (H<=2)):
    print("APROBADO")
else:
    print("Rechazado")