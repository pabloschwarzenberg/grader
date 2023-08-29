#Aprobación de créditos
Ingreso = float(input("Ingreso pesos:"))
AnnoNacimiento = int(input("Ingrese año de nacimiento:"))
Nhijos = int(input("Ingrese N° de hijos:"))
AnnoBanco = int(input("Años en banco:"))
EstadoCivil= input("Estado civil S:Soltero, C:Casado:")
while not(EstadoCivil =="S" or EstadoCivil == "C"):
    EstadoCivil= input("Estado civil S:Soltero, C:Casado")
CiudadCampo = input("U:Urbano o R:Rural:")
while not(CiudadCampo == "U" or CiudadCampo =="R"):
    CiudadCampo = input("U:Urbano o R:Rural:")

edad = 2020 - AnnoNacimiento

if(AnnoBanco >= 10 and Nhijos >= 2):
    print("APROBADO")
elif(EstadoCivil=="C" and Nhijos > 3 and (edad >= 45 and edad<= 55)):
     print("APROBADO")
elif(Ingreso >= 2500000 and EstadoCivil =="S" and CiudadCampo == "U"):
     print("APROBADO")    
elif(Ingreso >= 3500000 and  AnnoBanco > 5):
     print("APROBADO")    
elif(CiudadCampo == "R" and EstadoCivil == "C" and Nhijos < 2):
     print("APROBADO")       
elif(Ingreso >= 3500000 and  AnnoBanco > 5):
     print("APROBADO")    
else:
    print("RECHAZADO")
