#Zodíaco
dia = eval(input("Ingresar día: "))
mes = eval(input("Ingresar mes: "))

#Enero
if mes == 1:
  if dia < 20:
    print("Capricornio")
  else:
    print("Acuario")
#Febrero
elif mes == 2:
  if dia < 19:
    print("Acuario")
  else:
    print("Piscis")
#Marzo
elif mes == 3:
  if dia < 21:
    print("Piscis")
  else:
    print("Aries")
#Abril
elif mes == 4:
  if dia < 20:
    print("Aries")
  else:
    print("Tauro")
#Mayo
elif mes == 5:
  if dia < 21:
    print("Tauro")
  else:
    print("Geminis")
#Junio
elif mes == 6:
  if dia < 21:
    print("Geminis")
  else:
    print("Cancer")
#Julio
elif mes == 7:
  if dia < 23:
    print("Cancer")
  else:
    print("Leo")
#Agosto
elif mes == 8:
  if dia < 23:
    print("Leo")
  else:
    print("Virgo")
#Septiembre
elif mes == 9:
  if dia < 23:
    print("Virgo")
  else:
    print("Libra")
#Octubre
elif mes == 10:
  if dia < 23:
    print("Libra")
  else:
    print("Escorpio")
#Noviembre
elif mes == 11:
  if dia < 22:
    print("Escorpio")
  else:
    print("Sagitario")
#Diciembre
elif mes == 12:
  if dia < 22:
    print("Sagitario")
  else:
    print("Capricornio")