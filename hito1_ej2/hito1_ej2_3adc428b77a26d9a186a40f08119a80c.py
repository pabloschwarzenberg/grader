um = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese hora de la llamada: "))
if hora in range(0, 7):
     print("CONTESTAR")
elif hora < 14:
     if (num % 1000 == 9) and (num % 100 == 0) and (num % 10 == 9):
          print("CONTESTAR")
     else:
          print("NO CONTESTAR")
elif hora in range(17, 19):
     if (num % 100000000 == 8) and (num % 10000000 == 7) and (num % 1000000 == 7):
          print("NO CONTESTAR")
     else:
          print("CONTESTAR")
elif hora > 19:
     print("NO CONTESTAR")
