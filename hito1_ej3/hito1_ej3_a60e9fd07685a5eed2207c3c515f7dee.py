ing = int(input("Ingresos: "))
ano = int(input("Año: "))
hijos = int(input("Hijos: "))
anos_b = int(input("Años banco: "))
civil = input("Casado o Soltero: ")
lugar = input("Urbano o Rural")

if ((anos_b>10) and (hijos>=2)):
  print("APROBADO")
elif ((civil=="C") and (45<=(2022-ano)<=55) and (hijos>3)):
  print("APROBADO")
elif ((ing>=250000) and (civil=="S") and (lugar=="U")):
  print("APROBADO")
elif ((ing>=350000) and (anos_b>5)):
  print("APROBADO")
elif ((civil=="C") and (hijos<2) and (lugar=="R")):
  print("APROBADO")
else:
  print("NO APROBADO")


















    