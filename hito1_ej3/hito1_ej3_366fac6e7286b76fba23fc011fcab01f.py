I = int(input("ingrese sus ingresos (pesos):"))
A = int(input("ingrese su año de nacimiento:"))
edad = (2020 - A)
H = int(input("ingrese numero de hijos:"))
Anobanco = int(input("ingrese hace cuantos años pertenece al banco:"))


Estadocivil= input("¿Soltero (S) o Casado (C):")
    
CoC= input("¿Vive en localidad rural (R) o urbana (U):")


if(Anobanco>10) and (H>=2):
    print("APROBADO")
elif(Estadocivil=="C") and (H>3) and (edad>=45) and (edad<=55):
    print("APROBADO")
elif(I>2500000) and (Estadocivil=="S") and (CoC=="U"):
    print("APROBADO")
elif(I>3500000) and (Anobanco>5):
    print("APROBADO")
elif(CoC=="R") and (Estadocivil=="C") and (H<=2):
    print("APROBADO")
else:
    print("RECHAZADO")