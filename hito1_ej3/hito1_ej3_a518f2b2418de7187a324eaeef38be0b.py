#Aprobación de créditos
ingreso = int(input("Ingreso (en pesos) --> "))
nacimiento = int(input("Año de nacimiento --> "))
hijos = int(input("Número de hijos --> "))  
banco = int(input("Años de pertenencia al banco -->"))
estadocivil = str(input("Estado civil (S: soltero, C, casado) --> "))
vive = str(input("Si vive en campo o ciudad (U: urbano, R: rural) --> "))
 
                   
                   
                   
if (banco > 10) and (hijos >= 2):
                    print("APROBADO")
elif ((estadocivil.upper == "C") and (hijos > 3)) and (1964 < nacimiento < 1976 ):
                    print("APROBADO")                    
elif ((ingreso > 2500000) and (estadocivil.upper() == "S")) and (vive.upper() == "U"):
                    print("APROBADO")
elif (ingreso > 3500000) and (banco > 5):
                    print("APROBADO")                    
elif ((vive.upper() == "R") and (estadocivil.upper() == "C")) and (hijos == 1):
                    print("APROBADO")                    
else:
     print("RECHAZADO")    