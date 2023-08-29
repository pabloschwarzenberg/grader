#Aprobación de créditos
sueldo = int(input("Ingrese sueldo en pesos: "))
nacimiento= int(input("Ingrese Año de nacimiento: "))
numeroh = int(input("Ingrese numero de hijos: "))
anosbanco = int(input("Ingrese Años de pertenencia al banco: "))
ecivil = input("Ingrese Estado civil (S: soltero, C, casado): ")
vive = input("Ingrese Si vive en campo o cuidad (U: urbano, R: rural): ")

if(anosbanco > 10 and numeroh >= 2):
    print("APROBADO")
if(ecivil == "C" and numeroh > 3 and ((2021 - nacimiento)>=45 and (2021 - nacimiento) <= 55 )):
    print("APROBADO")
if(sueldo > 2500000 and ecivil == "S" and vive == "U" ):
    print("APROBADO")
if(sueldo > 3500000 and anosbanco > 5  ):
    print("APROBADO")
if(vive == "R" and  ecivil == "C" and numeroh < 2):
    print("APROBADO")    