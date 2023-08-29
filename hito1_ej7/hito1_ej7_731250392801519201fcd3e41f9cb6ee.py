#Zodiaco
print("ingresa tu fecha de cumpleaños:")
dia= int(input("dia: "))
mes= int(input("mes: "))
if dia >= 21 and mes == 3 or dia <= 20 and mes == 4:
   print("tu signo es aries")
else: 
     if dia >= 21 and mes == 4 or dia <= 21 and mes == 5:
        print("tu signo es tauro")
     else:
          if dia >= 22 and mes == 5 or dia <= 21 and mes == 6:
             print("tu signo es géminis")
          else:
               if dia >= 22 and mes == 6 or dia <= 22 and mes == 7:
                  print("tu signo es cáncer")
               else:
                     if dia >= 23 and mes == 7 or dia <= 22 and mes == 8:
                        print("tu signo es leo")
                     else:
                           if dia >= 23 and mes == 8 or dia <= 23 and mes == 9:
                              print("tu signo es virgo")
                           else:
                                 if dia >= 24 and mes == 9 or dia <= 23 and mes == 10:
                                    print("tu signo es libra")
                                 else:
                                       if dia >= 24 and mes == 10 or dia <= 22 and mes == 11:
                                          print("tu signo es escorpio")
                                       else:
                                            if dia >= 23 and mes == 11 or dia <= 21 and mes == 12:
                                               print("tu signo es sagitario")
                                            else:
                                                  if dia >= 22 and mes == 12 or dia <= 20 and mes == 1:
                                                      print("tu signo es capriconio")
                                                  else:
                                                        if dia >= 21 and mes == 1 or dia <= 19 and mes == 2:
                                                            print("tu signo es acuario")
                                                        else:
                                                              if dia >= 20 and mes == 2 or dia <= 20 and mes == 3:
                                                                 print("tu signo es piscis")