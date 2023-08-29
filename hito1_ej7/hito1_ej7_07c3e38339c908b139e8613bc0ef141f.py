#Zodiaco
diadenacimiento= int(input("Ingrese su dia de nacimiento: "))
mesdenacimiento= int(input("Ingrese su mes de nacimiento: "))
fechacompleta= int(mesdenacimiento*100+diadenacimiento)

if 321<=fechacompleta<=420:
  print("Aries")
elif 420<=fechacompleta<=521:
  print("Tauro")
elif 522<=fechacompleta<=621:
  print("Geminis")
elif 622<=fechacompleta<=722:
  print("Cancer")
elif 723<=fechacompleta<=822:
  print("Leo")
elif 823<=fechacompleta<=923:
  print("Virgo")
elif 924<=fechacompleta<=1023:
  print("Libra")
elif 1024<=fechacompleta<=1122:
  print("Escorpion")
elif 1123<=fechacompleta<=1221:
  print("Sagitario")
elif 121<=fechacompleta<=219:
  print("Acuario")
elif 220<=fechacompleta<=320:
  print("Piscis")
else:
  print("Capricornio")