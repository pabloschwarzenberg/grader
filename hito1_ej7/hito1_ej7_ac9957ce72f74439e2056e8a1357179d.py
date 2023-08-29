#Zodiacooooooo
d = eval(input("Birthday: "))
m = eval(input("Birth Month: "))
if((m == 3 and d >= 21 and d <= 31) or (m == 4 and d >= 1 and d <= 19)):
  print("Aries")
elif((m == 4 and d >= 20 and d <= 30)or(m == 5 and d >= 1 and d <= 20)):
  print("Tauro")
elif((m == 5 and d >= 21 and d <= 31)or(m == 6 and d >= 1 and d <= 21)):
  print("Geminis")
elif((m == 6 and d >= 22 and d <= 30)or(m == 7 and d >= 1 and d <= 22)):
  print("Cancer")
elif((m == 7 and d >= 23 and d <= 31)or(m == 8 and d >= 1 and d <= 23)):
  print("Leo")
elif((m == 8 and d >= 24 and d <= 31)or(m == 9 and d >= 1 and d <= 22)):
  print("Virgo")
elif((m == 9 and d >= 23 and d <= 30)or(m == 10 and d >= 1 and d <= 23)):
  print("Libra")
elif((m == 10 and d >= 24 and d <= 31)or(m == 11 and d >= 1 and d <= 22)):
  print("Escorpio")
elif((m == 11 and d >= 23 and d <= 30)or(m == 12 and d >= 1 and d <= 22)):
  print("Sagitario")
elif((m == 12 and d >= 23 and d <= 31)or(m == 1 and d >= 1 and d <= 20)):
  print("Capricornio")
elif((m == 1 and d >= 21 and d <= 31)or(m == 2 and d >= 1 and d <= 18)):
  print("Acuario")
elif((m == 2 and d >= 19 and d <= 28)or(m == 3 and d >= 1 and d <= 20)):
  print("Piscis")