#Aprobación de créditos
ingreso=eval(input("Registre sus ingresos en pesos:"))
nacimiento=eval(input("Registre su año de nacimiento:"))
hijos=eval(input("Registre cantidad de hijos o hijas:"))
pertenencia=eval(input("Registre sus años de pertenencia en el banco:"))
estado_civil=input("Registre su estado civil soltero (S) o casado (C):")
vivienda=input("Registre si vive en el campo(R) o la ciudad(U):")

# verificacion de edad

edad=(2021-nacimiento)

if(pertenencia>10)and(hijos>=2):
  print("APROBADO")

elif(estado_civil=="C")and(hijos>3)and(55>edad)and(edad>45):
  print("APROBADO")

elif(ingreso>2500000)and(estado_civil=="S")and(vivienda=="U"):
  print("APROBADO")

elif(ingreso>3500000)and(pertenencia>5):
  print("APROBADO")

elif(vivienda=="R")and(estado_civil=="C")and(hijos<2):
  print("APROBADO")

else:
  print("RECHAZADO")      