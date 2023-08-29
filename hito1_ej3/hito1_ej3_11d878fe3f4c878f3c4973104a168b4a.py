#Aprobación de créditos
Ingreso=float(input("ingrese su sueldo en pesos: "))
Nacimiento=int(input("ingrese su ano de nacimiento: "))
Hijos=int(input("ingrese su numero de hijos: "))
Antiguedad=int(input("cuantos anos lleva con este banco: "))
Estado_civil= str(input("ingrese s si es soltero o c si es casado: "))
Sector=str(input("ingrese u si vive en la ciudad o r si vive en el campo: "))
Edad= 2022-Nacimiento
if Antiguedad>10 and Hijos >= 2 :
          print("APROBADO")
elif (Estado_civil.upper()=="c" and Edad>=45 and Edad<=55):
  print("APROBADO")
elif (Ingreso > 2500000 and Estado_civil.upper() == "s" and Sector.upper() == "r") : 
  print ("APROBADO")
elif (Ingreso > 3500000 and Antiguedad > 5) : 
  print ("APROBADO") 
elif (Sector.upper() == "r" and Estado_civil.upper() == "c" and Hijos <2) : 
  print ("APROBADO")
else :
  print("REPROBADO")

