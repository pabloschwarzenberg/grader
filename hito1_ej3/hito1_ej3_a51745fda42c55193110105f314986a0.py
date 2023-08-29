#Aprobación de créditos

ingreso=int(input("Ingreso Mensual: "))
anacim=int(input("Año Nacimiento: "))
numhijos=int(input("Número Hijos: "))
abanco=int(input("Años de pertenencia al Banco: "))
estcivil=input("Estado Civil (S)oltero, (C)Asado: ")
vive=input("Donde Vive (U)rbano, (R)ural: ")

edad = 2022-anacim
strResult="RECHAZADO"

if abanco > 10 and numhijos >= 2:
   strResult="APROBADO"
elif estcivil.upper() == 'C' and numhijos > 3 and (edad >= 45 and edad <= 55):
   strResult="APROBADO"
elif ingreso > 2500000 and estcivil.upper() == "S" and vive.upper() == "U":
   strResult="APROBADO"
elif ingreso > 3500000 and abanco > 5:
   strResult="APROBADO"
elif vive.upper() == "R" and estcivil.upper() == "C" and numhijos < 2:
   strResult="APROBADO"

print(strResult)   