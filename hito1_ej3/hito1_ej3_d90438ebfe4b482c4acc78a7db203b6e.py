#Aprobación de créditos
Var_1 = eval(input("cuanto es su ingreso en pesos  " ))
Var_2 = eval(input("año de nacimiento   ")) 
Var_2 = 2021 - Var_2
Var_3 = eval(input("numero de hijos  "))
Var_4 = eval(input("cuantos años a pertenecido a nuestro banco  "))
Var_5 = str(input("cual es su estado civil S(soltero) o C(casado)  ")) 
Var_6 = str(input("usted vive en U(urbano) o R(rural)"))
if Var_4 > 10 :
  if Var_3 >= 2:
    print("APROBADO")
  else:
    print("RECHAZADO")
else:
  print("RECHAZADO")
if Var_5 == "C":
  if Var_3 > 3 :
    if Var_2 in range(45,55):
      print("APROBADO")
    else:
      print("RECHAZADO")
  else:
    print("RECHAZADO")
else:
  print("RECHAZADO")
if Var_1 > 250000:
  if Var_5 == "S": 
    if Var_6 == "U":
      print("RECHAZADO")
    else:
      print("RECHAZADO")
  else:
    print("RECHAZAO")
else:
  print("RECHAZADO")
if Var_1 > 3500000 and Var_4 > 5:
  print("APROBADO")
else:
  print("RECHAZADO")
if Var_6 == "R":
  if Var_5 == "C":
    if Var_3 < 2 :
      print("APROBADO")
    else:
      print("RECHAZADO")
  else:
    print("RECHAZADO")
else:
  print("RECHAZADO")
    
