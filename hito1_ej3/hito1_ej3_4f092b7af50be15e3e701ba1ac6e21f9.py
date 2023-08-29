#Aprobación de créditos
ingreso=int(input("Ingrese su sueldo: "))
anacimiento=int(input("Ingrese su año de nacimiento: "))
edad=2022-anacimiento
nhijo=int(input("Ingrese el numero de hijos: "))
anosbanco=int(input("Ingrese los años de pertenencia al banco: "))
ecivil=input("S: soltero, C, casado: ")
vive=input("U: urbano, R: rural: )")
if(anosbanco>10 and nhijo>2):
  print("APROBADO")
elif(ecivil=="c" and nhijo>=3 and 45<=edad>=55):
  print("APROBADO")
elif(ingreso>=2500000 and ecivil=="S" and vive=="U"):
  print("APROBADO")
elif(ingreso>=3500000 and anosbanco>5):
  print("APROBADO")
elif(vive=="R" and ecivil=="C" and nhijo<2):
  print("APROBADO")
else:
  print("RECHAZADO")