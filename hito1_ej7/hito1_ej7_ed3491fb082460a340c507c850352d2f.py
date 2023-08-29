#Zodiaco
dia = int(input("ingrese su dia de nacimiento"))
mes = int(input("ingrese su mes de naciminento"))

if (21 <= dia <= 31 and mes == 3) or ( 1 <= dia <= 20 and mes == 4):
   print("You are Aries")
elif (21 <= dia <= 30 and mes == 4) or ( 1 <= dia <= 21 and mes == 5):
   print("You are Tauro")
elif (22 <= dia <= 31 and mes == 5) or ( 1 <= dia <= 21 and mes == 6):
   print("You are Geminis")
elif (22 <= dia <= 30 and mes == 6) or ( 1 <= dia <= 22 and mes == 7):
   print("You are Cancer")
elif (23 <= dia <= 31 and mes == 7) or ( 1 <= dia <= 22 and mes == 8):
   print("You are Leo")
elif (23 <= dia <= 31 and mes == 8) or ( 1 <= dia <= 23 and mes == 9):
   print("You are Virgo")
elif (24 <= dia <= 30 and mes == 9) or ( 1 <= dia <= 23 and mes == 10):
   print("You are Libra")
elif (24 <= dia <= 31 and mes == 10) or ( 1 <= dia <= 22 and mes == 11):
   print("You are Escorpio")
elif (23 <= dia <= 30 and mes == 11) or ( 1 <= dia <= 21 and mes == 12):
   print("You are Sagitario")
elif (22 <= dia <= 31 and mes == 12) or ( 1 <= dia <= 20 and mes == 1):
   print("You are Capricornio")
elif (21 <= dia <= 31 and mes == 1) or ( 1 <= dia <= 19 and mes == 2):
   print("You are Acuario")
elif (20 <= dia <= 28 and mes == 2) or ( 1 <= dia <= 20 and mes == 3):
   print("You are Piscis")
else:
    print("You are aweonao, that day doesn't existe")