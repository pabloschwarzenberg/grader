#Zodiaco
dia=float(input("ingrese el día de cumpleaños en números enteros:"))
mes=float(input("ingrese el mes dde cumpleaños en números enteros:"))
if (21<=dia and mes==3) or (dia<=19 and mes==4):
 print("ARIES")
else:
 if (20<=dia and mes==4) or (dia<=20 and mes==5):
  print("TAURO")
 else:
  if (21<=dia and mes==5) or (dia<=20 and mes==6):
   print("GÉMINIS")
  else:
   if (21<=dia and mes==6) or (dia<=22 and mes==7):
    print("CÁNCER")
   else:
    if (23<=dia and mes==7) or (dia<=22 and mes==8):
     print("LEO")
    else:
     if (23<=dia and mes==8) or (dia<=22 and mes==9):
      print("VIRGO")
     else:
      if (23<=dia and mes==9) or (dia<=22 and mes==10):
       print("LIBRA")
      else:
       if (23<=dia and mes==10) or (dia<=21 and mes==11):
        print("ESCORPIO")
       else:
        if (22<=dia and mes==11) or (dia<=21 and mes==12):
         print("SAGITARIO")
        else:
         if (22<=dia and mes==12) or (dia<=19 and mes==1):
          print("CAPRICORNIO")
         else:
          if (20<=dia and mes==1) or (dia<=18 and mes==2):
           print("ACUARIO")
          else:
           if (19<=dia and mes==2) or (dia<=20 and mes==3):
            print("PISCIS")