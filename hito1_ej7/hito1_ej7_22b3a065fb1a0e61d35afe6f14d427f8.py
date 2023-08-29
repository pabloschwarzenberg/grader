dia = int(input("ingrese su dia de nacimiento: "))
mes = int(input("ingrese su mes de nacimiento: "))

if dia > 0 and mes > 0 and dia < 32 and mes < 13:
    if mes == 1:
        if dia > 20:
            print("Acuario")
        else:
            print("Capricornio")
    else:
        if mes == 2:
            if dia < 19:
                print("Acuario")
            else:
                print("Piscis")
        else:
             if mes == 3:
                if dia < 21:
                    print("Piscis")
                else:
                    print("Aries")
             else:
                 if mes == 4:
                     if dia < 21:
                        print("Aries")
                     else:
                          print("Tauro")
                 else:
                     if mes == 5:
                         if dia < 21:
                             print("Tauro")
                         else:
                             print("Geminis")
                     else:
                         if mes == 6:
                             if dia < 22:
                                 print("Geminis")
                             else:
                                 print("Cancer")
                         else:
                             if mes == 7:
                                 if dia < 23:
                                     print("Cancer")
                                 else:
                                     print("Leo")
                             else:
                                 if mes == 8:
                                     if dia < 23:
                                         print("Leo")
                                     else:
                                         print("Virgo")
                                 else:
                                     if mes == 9:
                                         if dia < 23:
                                             print("Virgo")
                                         else:
                                             print("Libra")
                                     else:
                                         if mes == 10:
                                             if dia < 23:
                                                 print("Libra")
                                             else:
                                                 print("Escorpio")
                                         else:
                                             if mes == 11:
                                                 if dia < 23:
                                                     print("Escorpio")
                                                 else:
                                                     print("Sagitario")
                                             else: 
                                                 if mes == 12:
                                                     if dia < 22:
                                                         print("Sagitario")
                                                     else:
                                                         print("Capricornio")
else:
     print("error")
      