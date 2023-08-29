#Aprobación de créditos
ing=eval(input("Ingrese monto de ingresos: "))
nac=eval(input("Ingrese año de nacimiento: "))
hijos=eval(input("Ingrese número de hijos: "))
ab=eval(input("Ingrese años de perteneciente al banco: "))
SC=input("Ingrese estado civil, Soltero (S) o Casado (C): ")
UR=input("Ingrese tipo de vivienda, Urbano(U) o Rural (R): ")

if ab>10 and hijos>=2:
    print("APROBADO")

elif (SC=="C" or SC=="c") and hijos>3 and nac>=1965 and nac<=1975:
    print("APROBADO")

elif ing>2500000 and (SC=="S" or SC=="s")  and (UR=="U" or UR=="u"):
    print("APROBADO")

elif ing>3500000 and ab>5:
    print("APROBADO")

elif  (UR=="R" or UR=="r") and (SC=="C" or SC=="c") and hijos<2:
    print("APROBADO")

else:
    print("RECHAZADO")