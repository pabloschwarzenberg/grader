#ENTRADA
ingreso=int(input("Ingreso mensual: $"))
anodenacimiento=int(input("Ingrese ano de nacimiento: "))
numerodehijos=int(input("cantidad de hijos:"))
banco= int(input("cuantos años lleva en el banco:"))
estadocivil= str(input("S:oltero o C:asado:"))
vivienda= str(input("Donde vive sector Rural o Urbano:" ))
edad= 2021- anodenacimiento

#DESARROLLO

if banco >=10 and numerodehijos >=2:  
    print("APROBADO")
elif str(estadocivil)[:1]=="c" and numerodehijos>=3 and edad>=45 and edad<55:
    print("APROBADO")
elif ingreso>=250000 and str(vivienda)[:1]=="u":
  print("APROBADO")
elif ingreso>=350000 and banco>5 :
   print("APROBADO")
elif str(estadocivil)[:1]=="c" and str(vivienda)[:1]=="r" and numerodehijos<=2:
  print("APROBADO")
else:
  print("RECHAZADO")