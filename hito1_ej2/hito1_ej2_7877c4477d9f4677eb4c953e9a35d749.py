#Contestador de celular

number = int(input("Número de 8 digitos:"))
while not(number>=10000000 and number<=99999999):
    number = int(input("ta Ta tA ta TÁ!, Número de 8 digitos:"))

hrs = int(input("La hora entre las 0 a las 23:"))
while not(hrs>=0 and hrs<=23):
    hrs = int(input("Hora invalida, entre las 0 a las 23:"))
ultimos3 = number%1000
primeros3 = number//100000

if (hrs<=7):
  print("CONTESTAR")
else:
  if (hrs<14):
    if (ultimos3 == 909):
      print("CONTESTAR")
    else:
      print("NO CONTESTAR")
  else:
     if (hrs<=19):
        if (hrs>=17 and hrs<=19):
            if (primeros3 == 877):
              print("NO CONTESTAR")
            else:
               print("CONTESTAR")
        else:
           print("NO CONTESTAR")
     else:
        print("NO CONTESTAR")