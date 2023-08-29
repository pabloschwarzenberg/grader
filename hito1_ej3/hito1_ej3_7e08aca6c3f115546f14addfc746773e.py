print("Para solicitar un credito ingrese los siguientes datos: ")
nombre=input("Ingrese su nombre: ")
sueldo=int(input("Ingrese su sueldo liquido: "))
edad=int(input("Ingrese su edad: "))
hijos=int(input("Ingrese n° de hijos: "))
antiguedad=int(input("Ingrese antiguedad en el banco: "))
estadocivil=input("Ingrese su estado civil: S para soltero o C para casado: ")
vivienda=str(input("Ingrese si vive en campo o ciudad: U para urbano o R para rural: "))

if antiguedad>10 and hijos>=2: 
  print("APROBADO")

elif estadocivil=="C" and hijos>3 and 55>=edad>=45: 
  print("APROBADO")

elif sueldo> 2500000 and estadocivil=="S" and vivienda=="U":
  print("APROBADO")

elif sueldo> 3500000 and antiguedad>5:
   print("APROBADO")

elif vivienda=="R" and estadocivil=="C" and hijos<2:
  print("APROBADO")

else:
  print("RECHAZADO")



