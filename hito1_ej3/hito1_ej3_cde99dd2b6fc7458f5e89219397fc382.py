#Aprobación de créditos
ingreso = int(input("ingrese su sueldo:  "))
ano = int(input("ingrese su año de nacimiento:  "))
hijo = int(input("ingrese la cantidad de hijos que tiene:  "))
banco = int(input("ingrese la cantidad de años que lleva en este banco:  "))
estado = input("ingrese S si es soltero o C si es casado:  ")
casa = input("ingrese U si vive en la ciudad o R si vive afuera de la ciudad:  ")
edad = (2022-ano)
if(banco>10 or hijo >=2):
  print("APROBADO")
elif(estado=="c" or estado=="C") and (hijo>3) and (edad>=45 or edad<=50):
  print("APROBADO")
elif(ingreso>2500000) and (estado=="s" or estado=="S") and (casa=="u" or casa=="U"):
  print("APROBADO")
elif(ingreso>3500000) and (banco>5):
  print("APROBADO")
elif (casa=="r" or casa=="R") and (estado=="c" or estado=="C") and (hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")