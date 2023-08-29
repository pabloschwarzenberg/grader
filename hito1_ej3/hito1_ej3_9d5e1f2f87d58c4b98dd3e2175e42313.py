#Aprobación de créditos
ingreso=float(input("Digite su ingreso mensual: "))
nacimiento=int(input("Digite el año de su nacimiento: "))
hijos=int(input("Digite la cantidad de hijos que tiene: "))
banco=int(input("Digite la cantidad de años desde que ha sido cliente del banco: "))
estado=input("¿Cuál es su estado civil? ¿Soltero o casado? Use S si es soltero y C si es casado: ")
vivienda=input("¿Vive usted en campo o ciudad? Use U si vive en ciudad, y R si vive en campo: ")

#Cálculo
edad=nacimiento-2022

if banco >= 10 and hijos >= 1:
  print ("APROBADO")

elif estado== "C" and hijos >= 3 and edad >=45 or edad==55:
  print ("APROBADO")

elif ingreso >=2500000 and estado=="S" and vivienda=="U":
  print("APROBADO")

elif ingreso >=3500000 and banco >= 5:
  print("APROBADO")

elif vivienda== "R" and estado== "C" and hijos <= 2:
  ("APROBADO")

else:
  print("RECHAZADO")