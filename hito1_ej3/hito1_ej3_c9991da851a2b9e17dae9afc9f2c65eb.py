ingreso= int(input("digite su ingreso en pesos:"))
anodenacimiento= int(input("ingrese año de nacimiento:"))
numerodehijos= int(input("ingrese numero de hijos:"))
anopertenenciaalbanco= int(input ("ingrese año de pertenencia:"))
estadocivil= input("ingrese S= soltero o C=casado:")
vivienda= input("ingrese U= urbano o R= rural :")
edad= 2020 - anodenacimiento
 
if (anopertenenciaalbanco > 10) and (numerodehijos>=2):
   print("APROBADO")
elif (estadocivil =="C") and (numerodehijos > 3)and (edad >= 45 and 55 >= edad):
   print("APROBADO")
elif (ingreso>2500000) and (estadocivil == "s") and (vivienda == "U"):
  print("APROBADO")
elif (ingreso>3500000) and (anopertenenciaalbanco>5):
   print("APROBADO")
elif (vivienda== "R") and (estadocivil=="C") and (2>numerodehijos):
   print("APROBADO")
else:
   print("RECHAZADO")