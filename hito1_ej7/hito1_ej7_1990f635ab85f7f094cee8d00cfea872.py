#Zodiaco
print("Que signo sodiacal eres")
Dia = int(input("Numero del dia que nació: "))
Mes = int(input("Numero del mes que nació: "))
if Mes == 1:
    if Dia >= 19:
        print("Acuario")
    else:
        print("Capricornio")
else:
    if Mes == 2:
        if Dia >= 19:
            print("Piscis")
        else:
            print("Acuario")
    else:
        if Mes == 3:
            if Dia >= 21:
                print("Aries")
            else:
                print("Piscis")
        else:
            if Mes == 4:
                if Dia >= 21:
                    print("Tauro")
                else:
                    print("Aries")
            else:
                if Mes == 5:
                    if Dia >= 21:
                        print("Geminis")
                    else:
                        print("Tauro")
                else:
                    if Mes == 6:
                        if Dia >= 23:
                            print("Cancer")
                        else:
                            print("Geminis")
                    else:
                        if Mes == 7:
                            if Dia >= 23:
                                print("Leo")
                            else:
                                print("Cancer")
                        else:
                            if Mes == 8:
                                if Dia >= 23:
                                    print("Virgo")
                                else:
                                    print("Leo")
                            else:
                                if Mes == 9:
                                    if Dia >= 23:
                                        print("Libra")
                                    else:
                                        print("Virgo")
                                else:
                                    if Mes == 10:
                                        if Dia >= 22:
                                            print("Escorpio")
                                        else:
                                            print("Libra")
                                    else:
                                        if Mes == 11:
                                            if Dia >= 22:
                                                print("Sagitario")
                                            else:
                                                print("Escorpio")
                                        else:
                                            if Mes == 12:
                                                if Dia >= 20:
                                                    print("Capricornio")
                                                else:
                                                    print("Sagitario")
                                            
        

