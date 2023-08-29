#Aprobación de créditos
ingreso = input("cuales son sus ingresos: ")
ano = input("su año de nacimiento: ")
hijos = input("cuantos hijos tiene: ")
abanco = input("cuantos años en el banco: ")
estado = input("si es soltero ingrese 'S', si es casado ingrese 'C': ")
vive = input("si vive en campo ingrese 'U', si vive en ciudad ingrese 'R': ")

if int(abanco) > 10 and int(hijos) >= 2:
  print("APROBADO")
elif estado == "C" and int(hijos) > 3 and 1966 > ano > 1976:
  print("APROBADO")
elif int(ingreso) > 2500000 and estado == "S" and vive == "U":
  print("APROBADO")
elif int(ingreso) > 3500000 and int(abanco) > 5:
  print("APROBADO")
elif vive == "R" and estado == "C" and int(hijos) < 2:
  print("APROBADO")
else:
  print("RECHAZADO")