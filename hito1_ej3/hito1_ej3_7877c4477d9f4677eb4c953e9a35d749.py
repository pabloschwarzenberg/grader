#Aprobación de créditos

ing = int(input("Ingrese su ingreso(?:"))
AAAAnac = int(input("Año de nacimiento:"))
numHijos = int(input("N° de hijos:"))
AAAAban = int(input("Año de permanencia al banco:"))
estCivil = str(input("Soltero(S) o Casado(C)?:"))
vivencia = str(input("Urbano(U) o Rural(R):"))
if(AAAAban>10 and numHijos>1):
    print("APROBADO")
elif(estCivil=='C' and numHijos>3) and (AAAAnac>45 and AAAAnac<55):
    print("APROBADO")
elif(ing>=2500000 and estCivil=='S' and vivencia=='U'):
    print("APROBADO")
elif(ing>=3500000 and AAAAban>5):
    print("APROBADO")
elif(vivencia=='R' and estCivil=='C' and numHijos<3):
    print("APROBADO")
else:
    print("RECHAZADO")