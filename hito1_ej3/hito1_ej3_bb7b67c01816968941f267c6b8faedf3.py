#Aprobación de créditos
ingr=eval(input("introduzca los ingresos : "))
anonacimiento=eval(input("ingrese el año de nacimiento : "))
ndehijos=eval(input("ingrese el numero de hijos : "))
anosenbanco=eval(input("ingrese los años de pertenencia al banco : "))
estadocivil=str(input("ingrese estado civil S o C : "))
campociudad=str(input("ingrese si vive en campo o ciudad donde U=urbano y R=rural : "))
edad=2020-anonacimiento
if(anosenbanco>10) and (ndehijos>=2):
  print("APROBADO")
elif(estadocivil=="C" and ndehijos>3 and edad>=45 and edad<=55):
  print("APROBADO")
elif(ingr>2500000 and estadocivil=="S" and campociudad=="U"):
  print("APROBADO")
elif(ingr>3500000 and anosenbanco>5):
  print("APROBADO")
elif(campociudad=="R" and estadocivil=="C" and ndehijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")  