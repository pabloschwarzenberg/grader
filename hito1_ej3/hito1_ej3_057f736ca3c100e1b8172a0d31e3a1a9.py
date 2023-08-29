#Aprobación de créditos
ING= int(input(" ingresos en pesos?:"))
APB= int(input("años de pertenencia al banco:"))
HI= int(input("cuantos hijos tiene:"))
FN= int(input("año de nacimiento:"))
EC= input("(S)soltero, (C)casado:") 
Z= input("vive en zona rural(R) o urbana(U):")
edad=2018-FN
if APB >10 and HI >=2:
 print("APROBADO")
elif ING > 2500000 and EC =="S" and Z =="U":
 print("APROBADO")
elif ING > 3500000 and APB > 5:
 print("APROBADO")
elif EC == "C" and HI > 3 and (edad<=55 and edad >=45):
 print("APROBADO")
elif Z == "R" and EC == "U" and HI < 2:
 print("APROBADO")
elif Z == "R" and EC == "C" and HI < 2:
 print("APROBADO")
else:
 print("RECHAZADO")
