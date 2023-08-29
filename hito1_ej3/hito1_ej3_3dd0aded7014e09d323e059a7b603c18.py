#Aprobación de créditos
ingreso=int(input("Ingrese el valor de su ingreso: "))
ano_nacimiento=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("Ingrese la cantidad de hijos que tiene: "))
banco=float(input("Ingrese la cantidad de años que ha pertenecido a nuestro banco: "))
estado=input("Ingrese una C si esta casado o una S si usted esta soltero: ")
vive=input("Ingrese una U si vive en la ciudad o una R si vive en el campo: ")

if banco>10 and hijos>=2:
  print("APROBADO")
elif (estado[0]=="C") and (hijos>3) and (55>(2017-ano_nacimiento)>45):
  print("APROBADO")
elif (ingreso>2500000) and (estado[0]=="S") and (vive[0]=="U"):
  print("APROBADO")
elif (ingreso>3500000) and (banco>5):
  print("APROBADO")
elif (vive[0]=="R") and (estado[0]=="C") and (hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")