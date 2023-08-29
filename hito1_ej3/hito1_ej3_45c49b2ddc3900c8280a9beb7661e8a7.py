#Aprobación de créditos
Ingreso=int(input("Indique su ingreso (en pesos)"))
Anacimiento=int(input("Ingrese su año de nacimiento:"))
Hijos=int(input("ingrese el numero de hijos que tiene: "))
Permanencia=int(input("ingrese los años de permanencia al banco: "))
Ecivil=input("ingrese Estado civil (S: soltero, C, casado): ")
Localidad=(input("Si vive en campo o cuidad (U: urbano, R: rural: "))
Edad=2022-Anacimiento
if(Permanencia>10 and Hijos>=2):
  print("APROBADO")
elif(Ecivil=="C" and Hijos>3 and Edad>44 and Edad<56):
  print("APROBADO")
elif(Ingreso>2500000 and Ecivil=="s" and Localidad=="u"):
  print("APROBADO")
elif(Ingreso>3500000 and Permanencia>5):
  print("APROBADO")
elif(Localidad=="R" and Ecivil=="C" and Hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")