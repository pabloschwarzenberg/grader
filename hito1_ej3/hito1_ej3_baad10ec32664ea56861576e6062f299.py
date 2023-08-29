#Aprobación de créditos
ingreso = int(input("Ingrese su ingreso mensual :"))
a_nac = int(input("Ingrese año de nacimiento :"))
numhijos = int(input("Ingrese cantidad de hijos :"))
permanencia = int(input("Ingrese los años de permanencia en el banco :"))
estadocivil = input("Ingrese su estado civil (S):soltero (C):casado:")
lugar = input("Ingrese lugar donde vive(U) urbano, (R) rural:")

edad = 2022 - a_nac

if(permanencia > 10 and numhijos > 1):
    print("APROBADO")
elif(estadocivil == "C" and numhijos > 3 and (edad > 44 and edad < 56)):
     print("APROBADO")
elif(ingreso > 2500000 and estadocivil == "S" and lugar == "U"):
    print("APROBADO")
elif(ingreso > 3500000 and permanencia > 5):    
    print("APROBADO")
elif(lugar == "R" and estadocivil == "C" and numhijos < 2):
     print("APROBADO")
else:
    print("RECHAZADO")