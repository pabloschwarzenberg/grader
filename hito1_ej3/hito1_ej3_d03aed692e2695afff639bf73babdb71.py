#Aprobación de créditos
ingreso = int(input("ingrese su ingreso en pesos: "))
nacimiento = int(input("ingrese su año de nacimiento: "))
hijos = int(input("ingrese numero de hijos: "))
annos = int(input("ingrese cantidad de años como cliente del banco: "))
estadocivil = str(input("ingrese 'S' si es soltero o 'C' si es casado: "))
residencia = str(input("ingrese 'U' si vive en ciudad o 'R' si vive en campo: "))
edad=2018-nacimiento
if annos>10 and hijos>=2:
  print("APROBADO")
elif estadocivil=="C" and hijos>3 and 45<edad<55:
  print("APROBADO")
elif ingreso>2500000 and estadocivil=="S" and residencia=="U":
  print("APROBADO")
elif ingreso>3500000 and annos>5:
  print("APROBADO")
elif residencia=="R" and estadocivil=="C" and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")