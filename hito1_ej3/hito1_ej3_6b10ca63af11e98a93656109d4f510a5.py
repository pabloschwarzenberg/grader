#Aprobación de créditos
Ingreso = int(input("ingresos:"))
Nacimiento = int(input("año de nacimiento:"))
Hijos = int(input("numero de hijos:")) 
AnosEnElBanco = int(input("años de pertenencia en el banco:"))
EstadoCivil = str(input("eres Soltero (S) o Casado (C):"))
CampoOCiudad = str(input("vives en el Campo (R) o en la Ciudad (U):"))

Ano_Actual = 2000 
Edad = Ano_Actual - Nacimiento

if AnosEnElBanco > 10 and Hijos >= 2:
    print("APROBADO")

elif str(EstadoCivil) == "C" and Hijos > 3 and Edad > 45 and Edad < 55:
    print("APROBADO")

elif Ingreso >  2500000 and str(EstadoCivil) == "S" and str(CampoOCiudad) == "U":
    print("APROBADO")

elif Ingreso > 3500000 and AnosEnElBanco >  5:
    print("APROBADO")

elif str(CampoOCiudad) == "R" and str(EstadoCivil) == "C" and Hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
