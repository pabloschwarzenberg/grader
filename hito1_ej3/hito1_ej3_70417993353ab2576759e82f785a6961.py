#Aprobación de créditos
I= int(input("Cantidad de ingresos en pesos: "))
ADN = int(input("Ingrese su año de nacimiento:"))
AA= 2021 - ADN
NH= int(input("¿Ingrese cuantos hijos tiene?: "))
A_con_el_banco = int(input("¿Cuantos años ha sido cliente en nuestro banco?: "))
EC= str(input("Por favor indique su estado civil (S si soltero o C si esta casado: "))
vivienda = str(input("Si vive en un sector rural marque R o, si es un sector urbano, una U: "))
if NH >= 2 and A_con_el_banco > 10:
  print("APROBADO")
elif EC == "C" and NH > 3 and AA <= 55 and AA >=45:
  print("APROVADO")
elif I >= 2500000 and EC == "S" and vivienda == "u":
  print("APROBADO")
elif vivienda == "R" and EC == "C" and NH < 2:
  print("APROBADO")
elif I > 3500000 and A_con_el_banco > 5:
  print("APROBADO")
else:
  print ("RECHAZADO")
