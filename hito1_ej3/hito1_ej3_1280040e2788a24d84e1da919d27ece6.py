#Aprobación de créditos
ingresos=float(input("Ingreso (en pesos) "))
añonacimiento=float(input("Año de nacimiento "))
numerohijos=float(input("Número de hijos "))
añobanco=float(input("Años de pertenencia al banco "))
estadocivil=str(input("Estado civil ('S': soltero, 'C', casado) "))
zona=str(input("Si vive en campo o cuidad ('U': urbano, 'R': rural) "))

edad=2020-añonacimiento

if (añobanco>=10 and numerohijos>=2 or estadocivil[0]== "C" and numerohijos>=3 and edad>=45 and edad<=55 or ingresos>2500000 and estadocivil[0]=="S" and zona[0]=="U" or ingresos>3500000 and añobanco>=5 or zona[0]=="R" and estadocivil[0]=="C" and numerohijos<2):  
  print("APROBADO")
else:
  print ("RECHAZADO")
      