ingreso=int(input("Ingreso:"))
ano=int(input("Año de nacimiento:"))
hijos=int(input("Número de hijos:"))
banco=int(input("Años de pertenencia al banco:"))
civil=input("Estado civil:")
vivienda=input("Vives en campo o ciudad?:")
if banco>10 or hijos>=2:
  print("APROBADO")
elif civil==c and hijos>3 and 1963<ano<1973:
  print("APROBADO")
elif ingreso>2500000 and civil==s and vivienda==u:
  print("APROBADO")
elif ingreso>3500000 and banco>5:
  print("APROBADO")
elif vivienda==r and civil==c and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")