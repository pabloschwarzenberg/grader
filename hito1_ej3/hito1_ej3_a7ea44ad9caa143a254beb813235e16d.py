ingreso=int(input("indique su ingreso (en pesos)"))
anaci=int(input("ingrese su año de nacimiento:"))
hijos=int(input("ingrese el numero de hijos que tiene: "))
permanencia=int(input("ingrese los años de permanencia al banco: "))
ecivil=input("ingrese Estado civil (S: soltero, C, casado): ")
localidad=(input("Si vive en campo o cuidad (U: urbano, R: rural: "))
edad=2022-anaci
if(permanencia>10 and hijos>=2):
  print("APROBADO")
elif(ecivil=="C" and hijos>3 and edad>44 and edad<56):
  print("APROBADO")
elif(ingreso>2500000 and ecivil=="s" and localidad=="u"):
  print("APROBADO")
elif(ingreso>3500000 and permanencia>5):
  print("APROBADO")
elif(localidad=="R" and ecivil=="C" and hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")