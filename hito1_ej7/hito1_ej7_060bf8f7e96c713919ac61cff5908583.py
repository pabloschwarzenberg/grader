dia = int(input())
mes = int(input())

if dia >= 21 and mes == 3  or dia <= 20 and mes ==4:
  print("aries")
elif dia >= 20 and mes == 4 or dia <= 21 and mes ==5:
  print("tauro")
elif dia >= 21 and mes == 5 or dia <= 21 and mes == 6:
  print("geminis")
elif dia >= 21 and mes == 6 or dia <= 21 and mes == 7:
  print("cancer")
elif dia >= 23 and mes == 7 or dia <= 23 and mes == 8:
  print("leo")
elif dia >= 23 and mes == 8 or dia <= 23 and mes == 9:
  print('virgo')
elif dia >= 23 and mes == 9 or dia <= 23 and mes == 10:
  print('libra')
elif dia >= 23 and mes == 10 or dia <= 22 and mes == 11:
  print('escorpion')
elif dia >= 23 and mes == 11 or dia <= 22 and mes == 12:
  print('Sagitario')
elif dia >= 22 and mes == 12 or dia <= 20 and mes == 1:
  print('Capricornio')
elif dia >= 20 and mes == 1 or dia <= 19 and mes == 2:
  print('acuario')
elif dia >= 19 and mes == 2 or dia <= 21 and mes == 3:
  print('Piscis')