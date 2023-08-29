#Ordenar tres números
#Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma.
#entrada:
pri=int(input("escriba el primer N°:"))
seg=int(input("escriba el segundo N°:"))
ter=int(input("escriba el tercer N°:"))
#desarrollo:
if pri==seg and pri==ter:
  print(str(pri)+","+str(seg)+","+str(ter))
elif pri==seg and ter<pri:
  print(str(ter)+","+str(pri)+","+str(seg))
elif pri<ter and pri==seg:
  print(str(pri)+","+str(seg)+","+str(ter))
elif pri==ter and seg<pri:
  print(str(seg)+","+str(pri)+","+str(ter))
elif pri<seg and pri==ter:
  print(str(pri)+","+str(ter)+","+str(seg))
elif pri<seg and seg==ter:
  print(str(pri)+","+str(seg)+","+str(ter))
elif seg<pri and seg==ter:
  print(str(seg)+","+str(ter)+","+str(pri))
elif seg<ter and seg==pri:
  print(str(seg)+","+str(pri)+","+str(ter))
elif seg<pri and ter<seg:
  print(str(ter)+","+str(seg)+","+str(pri))
elif pri<ter and seg<pri:
  print(str(seg)+","+str(pri)+","+str(ter))
elif ter<seg and pri<ter:
  print(str(pri)+","+str(ter)+","+str(seg))
elif ter<pri and seg<ter:
  print(str(seg)+","+str(ter)+","+str(pri))
elif pri<seg and ter<pri:
  print(str(ter)+","+str(pri)+","+str(seg))
elif seg<ter and pri<seg:
  print(str(pri)+","+str(seg)+","+str(ter))