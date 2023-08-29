#Zodiaco
D = float(input("Ingrese el día de cumpleaños en números enteros: "))
M = float(input("Ingrese el mes de cumpleaños en números enteros: "))
if (21 <= D and M == 3) or (D <= 19 and M == 4):
 print("ARIES")
else:
 if (20 <= D and M == 4) or (D <= 20 and M == 5):
  print("TAURO")
 else:
  if (21 <= D and M == 5) or (D <= 20 and M == 6):
   print("GÉMINIS")
  else:
   if (21 <= D and M == 6) or (D <= 22 and M == 7):
    print("CÁNCER")
   else:
    if (23 <= D and M == 7) or (D <= 22 and M == 8):
     print("LEO")
    else:
     if (23 <= D and M == 8) or (D <= 22 and M == 9):
      print("VIRGO")
     else:
      if (23 <= D and M == 9) or (D <= 22 and M == 10):
       print("LIBRA")
      else:
       if (23 <= D and M == 10) or (D <= 22 and M == 11):
        print("ESCORPIO")
       else:
        if (23 <= D and M == 11) or (M <= 21 and M == 12):
         print("SAGITARIO")
        else:
         if (22 <= D and M == 12) or (D <= 19 and M == 1):
          print("CAPRICORNIO")
         else:
          if (20 <= D and M == 1) or (D <= 18 and M == 2):
           print("ACUARIO")
          else:
           if (19 <= D and M == 2) or (D <= 20 and M == 3):
            print("PISCIS")

