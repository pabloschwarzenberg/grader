dia = eval(input("ingrese dia de nacimiento: "))
mes = eval(input("ingrese mes de nacimiento: "))
if (21 <= dia <= 31) and (mes == 3 ) or(dia < 20) and (mes == 4):
  print("eres aries")
elif (20 <= dia <= 30) and (mes == 4) or (dia < 21) and (mes == 5):
  print("eres tauro")
elif (21 <= dia <= 31) and (mes == 5) or (dia < 21) and (mes == 6):
  print("eres geminis")
elif (21 <= dia <= 30) and (mes == 6) or (dia < 23) and (mes == 7):
  print("eres cancer")
elif (23 <= dia <= 31) and (mes == 7) or (dia < 23) and (mes == 8):
  print("eres leo")
elif (23 <= dia <= 31) and (mes == 8) or (dia < 23) and (mes == 9):
  print("eres virgo")
elif (23 <= dia <= 30) and (mes == 9) or (dia < 23) and (mes == 10):
  print("eres libra")
elif (23 <= dia <= 31) and (mes == 10) or (dia <= 22) and (mes == 11):
  print("eres escorpio")
elif (23 <= dia <= 30) and (mes == 11) or (dia < 22) and (mes == 12):
  print("eres sagitario")
elif (22 <= dia <= 31) and (mes == 12) or (dia < 20) and (mes == 1):
  print("eres capricornio")
elif (20 <= dia <= 31) and (mes == 1) or (dia < 19) and (mes == 2):
  print("eres acuario")
elif (19 <= dia <= 28) and (mes == 2) or (dia < 21) and (mes == 3):
  print("eres piscis")   