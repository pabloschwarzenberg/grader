#Aprobación de créditos
ingreso = eval(input("Su ingreso es (sin ptos):$"))
anho     = eval(input("Año de nacimiento:"))
hijos   = eval(input("Numero de hijos:"))
banco   =eval(input("Años de pertenencia al Banco:"))
civil   =input("Estado civil // Soltero(S) - Casado(C):")
vive    =input("La ubicacion de su vivienda // Urbano(U) o Rural(R)")
anho_actual=2020
edad = 2020 - anho
if(banco>=10 and hijos>= 2):
  print("APROBADO")
elif(civil=="C" and hijos>=3 and edad>45 and edad<55):
  print("APROBADO")
elif(ingreso > 2500000 and civil=="S" and vive=="U"):
  print("APROBADO")
elif(ingreso>3500000 and banco>5):
  print("APROBADO")
elif(vive=="R" and civil=="C" and hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")  