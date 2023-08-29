#Aprobación de créditos
#Aprobación de créditos

I=eval(input("Ingrese monto de ingresos: "))
A=eval(input("Ingrese año de nacimiento: "))
H=eval(input("Ingrese número de hijos: "))
AB=eval(input("Ingrese años de perteneciente al banco: "))
SC=input("Ingrese estado civil, Soltero (S) o Casado (C): ")
UR=input("Ingrese tipo de vivienda, Urbano(U) o Rural (R): ")

if AB>10 and H>=2:
    print("APROBADO")

elif (SC=="C" or SC=="c") and H>3 and A>=1965 and A<=1975:
    print("APROBADO")

elif I>2500000 and (SC=="S" or SC=="s")  and (UR=="U" or UR=="u"):
    print("APROBADO")

elif I>3500000 and AB>5:
    print("APROBADO")

elif  (UR=="R" or UR=="r") and (SC=="C" or SC=="c") and H<2:
    print("APROBADO")

else:
    print("RECHAZADO")

