#Aprobación de créditos
ingreso = int(input("Ingreso: "))
nacimiento = 2023 - int(input("Año de nacimiento: "))
hijos = int(input("Numero de hijos: "))
antiguedad = int(input("Años de pertenencia al banco: "))
estadoC = input("Estado civil: ")
locacion = input("Locacion: ")


if antiguedad>10 and hijos>= 2:
  print("APROBADO")
elif estadoC=="C" and hijos>3 and nacimiento>45 and nacimiento<55:
  print("APROBADO")
elif ingreso>2500000 and estadoC=="S" and locacion=="U":
  print("APROBADO")
elif ingreso>3500000 and antiguedad>5:
  print("APROBADO")
elif locacion=="R" and estadoC=="C" and hijos<2:
    print("APROBADO")
 
 