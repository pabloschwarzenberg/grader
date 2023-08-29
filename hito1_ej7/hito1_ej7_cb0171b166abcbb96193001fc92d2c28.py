#Zodiaco
dia = int(input('ingresa dia de cumpleaños:'))
mes = int(input('ingresa mes de cumpleaños:'))

if   1 <= dia <= 31 and 1<= mes <= 12:
  if (21 <= dia and mes == 3) or (dia <= 19 and mes == 4):
   print('Aries')
  else:
   if (20 <= dia and mes == 4) or (dia <= 20 and mes == 5):
    print('Tauro')
   else:
    if (21 <= dia and mes == 5) or (dia <= 20 and mes == 6):
     print('Geminis')
    else:
     if (21 <= dia and mes == 6) or (dia <= 22 and mes == 7):
      print('Cancer')
     else:
      if (23 <= dia and mes == 7) or (dia <= 22 and mes == 8):
       print('Leo')
      else:
       if (23 <= dia and mes == 8) or (dia <= 22 and mes == 9):
        print('Virgo')
       else:
        if (23 <= dia and mes == 9) or (dia <= 22 and mes == 10):
         print('Libra')
        else:
         if (23 <= dia and mes == 10) or (dia <= 21 and mes == 11):
          print('Escorpio')
         else:
          if (22 <= dia and mes == 11) or (dia <= 21 and mes == 12):
           print('Sagitario')
          else:
           if (22 <= dia and mes == 12) or (dia <= 19 and mes == 1):
            print('Capricornio')
           else:
            if (20 <= dia and mes == 1) or (dia <= 18 and mes == 2):
             print('Acuario')
            else:
             if (19 <= dia and mes == 2)or (dia <= 20 and mes == 3):
              print('Piscis')


