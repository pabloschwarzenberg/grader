#Contestador de celular
num = int(input("Número: "))
hr = int(input("Hora de llamada: "))
snum = str(num)
#Si son las 7 o antes
if hr <= 7:
  print("CONTESTAR")
#Si termina en 909
elif hr < 14:
  if "909" == (snum[5] + snum[6] + snum[7]):
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
#Si son entre las 17 y 19, excepto si comienza con 877
elif hr > 17 and hr < 19:
  if 877 != int(snum[0] + snum[1] + snum[2]):
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
#Despues de las 19
elif hr > 19:
  print("NO CONTESTAR")