#Aprobación de créditos
ingreso=int(input("ingrese su ingreso en pesos:"))
anonacimiento=int(input("ingrese su año de nacimiento:"))
hijos=int(input("ingrese su numero de hijos:"))
anobanco=int(input("ingrese sus años de pertenencia en el banco:"))
estado=input("ingrese su estado civil, escriba S si está soltero y C si está casado:")
lugar=input("ingrese si vive en el campo o cuidad, escriba R si vive en el campo y U si vive en la ciudad:")

if(anobanco>10 and hijos>=2):
  print("APROBADO")
elif(estado=="C" and hijos>3 and 1963<=anonacimiento<=1973):
  print("APROBADO")
elif(ingreso>2500000 and estado=="S" and lugar=="U"):
  print("APROBADO")
elif(ingreso>3500000 and anobanco>5):
  print("APROBADO")
elif(lugar=="R" and estado=="C" and hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")