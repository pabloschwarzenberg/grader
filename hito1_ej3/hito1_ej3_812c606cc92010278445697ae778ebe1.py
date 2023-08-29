#Aprobación de créditos
ing=int(input("Ingrese su ingreso en pesos: "))
anonac=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("Ingrese su numero de hijos: "))
anobanco=int(input("Ingrese sus años de pertenencia al banco: "))
estadocivil=input("Ingrese su estado civil, Siendo soltero representado por una S y casado representado por una C: ")
vive=input("Ingrese su zona donde vive, siendo rural representado por una R y urbano siendo representado por una U: ")
edad=2020-anonac
if anobanco>10 and hijos>=2:
  print("APROBADO ")
elif estadocivil=="C" and hijos>3 and edad>=45 and edad<=55:
  print("APROBADO ")
elif ing>2500000 and estadocivil=="S" and vive=="U":
  print("APROBADO ")
elif ing>3500000 and anobanco>5:
  print("APROBADO ")
elif vive=="R" and estadocivil=="C" and hijos<2:
  print("APROBADO ")
else:
   print("RECHAZADO ")