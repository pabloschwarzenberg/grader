#aprobacion de creditos
ingreso=int(input("¿Cuál es tu ingreso en pesos?"))
nacimiento=int(input("¿Cuál es tu año de nacimiento?"))
hijos=int(input("¿Cuántos hijos tienes?"))
pertenencia=int(input("¿Cuántos años de pertenencia llevas en el banco?"))
estado=input("¿Cuál es tu estado civil?")
C="casado"
S="soltero"
vive=input("¿Vives en sector urbano o rural?")
U="urbano"
R="rural"
if(pertenencia > 10 and hijos >= 2):
  print("APROBADO")
elif(estado == "C" and hijos > 3 and nacimiento >= 1966 or nacimiento <= 1976):
  print("APROBADO")
elif(ingreso > 2500000 and estado == "S" and vive == "U"):
  print("APROBADO")
elif(ingreso > 3500000 and pertenencia > 5):
  print("APROBADO")
elif(vive == "R" and estado == "C" and hijos < 2):
  print("APROBADO")
else:
  print("RECHAZADO")

