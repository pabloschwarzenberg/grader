#Zodiaco
a=int(input("Día:"))
b=int(input("Mes:"))
if(b==4):
    if(1<=a<=20):print("Aries")
    else:
        if(21<=a<=30):print("Taurus")
        else:print("Fecha no válida")
else:
    if(b==5):
        if(1<=a<=21):print("Taurus")
        else:
            if(22<=a<=31):print("Gemini")
            else:print("Fecha no válida")
    else:
        if(b==6):
            if(1<=a<=21):print("Gemini")
            else:
                if(22<=a<=30):print("Cancer")
                else:print("Fecha no válida")
        else:
            if(b==7):
               if(1<=a<=22):print("Cancer")
               else:
                   if(23<=a<=31):print("Leo")
                   else:print("Fecha no válida")
            else:
                if(b==8):
                   if(1<=a<=22):print("Leo")
                   else:
                       if(23<=a<=31):print("Virgo")
                       else:print("Fecha no válida")
                else:
                    if(b==9):
                       if(1<=a<=23):print("Virgo")
                       else:
                           if(24<=a<=30):print("Libra")
                           else:print("Fecha no válida")
                    else:
                        if(b==10):
                           if(1<=a<=23):print("Libra")
                           else:
                               if(24<=a<=31):print("Scorpio")
                               else:print("Fecha no válida")
                        else:
                            if(b==11):
                               if(1<=a<=22):print("Scorpio")
                               else:
                                   if(23<=a<=30):print("Sagittarius")
                                   else:print("Fecha no válida")
                            else:
                                if(b==12):
                                   if(1<=a<=21):print("Sagittarius")
                                   else:
                                       if(22<=a<=31):print("Capricorn")
                                       else:print("Fecha no válida")
                                else:
                                    if(b==1):
                                       if(1<=a<=20):print("Capricorn")
                                       else:
                                           if(21<=a<=31):print("Aquarius")
                                           else:print("Fecha no válida")
                                    else:
                                        if(b==2):
                                           if(1<=a<=19):print("Aquarius")
                                           else:
                                               if(20<=a<=29):print("Pisces")
                                               else:print("Fecha no válida")
                                        else:
                                            if(b==3):
                                               if(1<=a<=20):print("Pisces")
                                               else:
                                                   if(21<=a<=30):print("Aries")
                                                   else:print("Fecha no válida")